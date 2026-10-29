"""
Dashboard Statistik Deskriptif - Statistik dan Probabilitas 1 (Pertemuan 4)

Jalankan dari terminal (di dalam folder ini):
    streamlit run app.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

# ======================================================================
# 1. KONFIGURASI HALAMAN
# ======================================================================
st.set_page_config(page_title="Dashboard StatPro 1", page_icon="📊", layout="wide")

DATA_DEFAULT = Path(__file__).parent / "data" / "data_mahasiswa.csv"


# ======================================================================
# 2. FUNGSI BANTU
# ======================================================================
@st.cache_data
def muat_data_default(path):
    """Baca CSV bawaan. Di-cache supaya tidak dibaca ulang setiap interaksi."""
    return pd.read_csv(path)


def hitung_statistik(x: pd.Series) -> dict:
    """Hitung seluruh ukuran statistik deskriptif untuk satu kolom."""
    q1, q3 = x.quantile(0.25), x.quantile(0.75)
    iqr = q3 - q1
    batas_bawah = q1 - 1.5 * iqr
    batas_atas = q3 + 1.5 * iqr
    return {
        "n": len(x),
        "mean": x.mean(),
        "median": x.median(),
        "modus": list(x.mode()),
        "std": x.std(),                       # sampel (ddof=1)
        "min": x.min(),
        "max": x.max(),
        "q1": q1,
        "q3": q3,
        "iqr": iqr,
        "batas_bawah": batas_bawah,
        "batas_atas": batas_atas,
        "outlier": x[(x < batas_bawah) | (x > batas_atas)],
    }


def format_modus(daftar, maks_tampil=3):
    teks = ", ".join(f"{m:g}" for m in daftar[:maks_tampil])
    return teks + (" ..." if len(daftar) > maks_tampil else "")


# ======================================================================
# 3. SIDEBAR: SUMBER DATA, PILIH KOLOM, FILTER
# ======================================================================
st.sidebar.title("⚙️ Pengaturan")

file_upload = st.sidebar.file_uploader("Upload CSV sendiri (opsional)", type="csv")
if file_upload is not None:
    df = pd.read_csv(file_upload)
    st.sidebar.success("Memakai file upload")
else:
    df = muat_data_default(DATA_DEFAULT)
    st.sidebar.info("Memakai data_mahasiswa.csv")

kolom_numerik = df.select_dtypes(include="number").columns.tolist()
kolom_kategori = [
    k for k in df.select_dtypes(exclude="number").columns if df[k].nunique() <= 10
]

if not kolom_numerik:
    st.error("File ini tidak punya kolom numerik. Coba upload file lain.")
    st.stop()

kolom = st.sidebar.selectbox("Kolom yang dianalisis", kolom_numerik)

st.sidebar.subheader("Filter data")
df_f = df.copy()
for k in kolom_kategori:
    semua = sorted(df[k].dropna().unique())
    pilihan = st.sidebar.multiselect(f"{k}", semua, default=semua)
    df_f = df_f[df_f[k].isin(pilihan)]

x = df_f[kolom].dropna()
if x.empty:
    st.warning("Tidak ada data setelah difilter. Longgarkan filter di sidebar.")
    st.stop()

stat = hitung_statistik(x)


# ======================================================================
# 4. HALAMAN UTAMA
# ======================================================================
st.title("📊 Dashboard Statistik Deskriptif")
st.caption(f"Kolom: **{kolom}** | Data terpilih: {len(df_f)} dari {len(df)} baris")

tab_data, tab_stat, tab_vis, tab_dadu = st.tabs(
    ["📋 Data", "🧮 Statistik", "📈 Visualisasi", "🎲 Simulasi Dadu"]
)

# ----------------------------- TAB DATA -------------------------------
with tab_data:
    c1, c2, c3 = st.columns(3)
    c1.metric("Jumlah baris", len(df_f))
    c2.metric("Jumlah kolom", df_f.shape[1])
    c3.metric("Data kosong (total)", int(df_f.isna().sum().sum()))

    st.dataframe(df_f, width="stretch")

    with st.expander("Lihat data kosong per kolom"):
        st.dataframe(df_f.isna().sum().rename("Jumlah kosong"))

# --------------------------- TAB STATISTIK ----------------------------
with tab_stat:
    st.subheader("Ukuran Pemusatan")
    a, b, c, d = st.columns(4)
    a.metric("Mean", f"{stat['mean']:.2f}")
    b.metric("Median", f"{stat['median']:.2f}")
    c.metric("Modus", format_modus(stat["modus"]))
    d.metric("Jumlah data (n)", stat["n"])

    st.subheader("Ukuran Penyebaran")
    e, f, g, h = st.columns(4)
    e.metric("Std Dev (sampel)", f"{stat['std']:.2f}")
    f.metric("Range", f"{stat['max'] - stat['min']:.2f}")
    g.metric("IQR", f"{stat['iqr']:.2f}")
    h.metric("Jumlah outlier", len(stat["outlier"]))

    # Interpretasi otomatis: bandingkan mean dan median
    selisih = stat["mean"] - stat["median"]
    if abs(selisih) < 0.1 * stat["std"]:
        st.success("Mean ≈ Median → distribusi relatif **simetris**.")
    elif selisih > 0:
        st.info("Mean > Median → distribusi **condong ke kanan** (ada nilai besar yang menarik mean).")
    else:
        st.info("Mean < Median → distribusi **condong ke kiri** (ada nilai kecil yang menarik mean).")

    with st.expander("Detail kuartil dan batas outlier (aturan 1,5 × IQR)"):
        st.write(f"Q1 = {stat['q1']:.2f} | Q3 = {stat['q3']:.2f}")
        st.write(f"Batas bawah = {stat['batas_bawah']:.2f} | Batas atas = {stat['batas_atas']:.2f}")
        if len(stat["outlier"]) > 0:
            st.write("Nilai outlier:", stat["outlier"].tolist())
        else:
            st.write("Tidak ada outlier.")

    st.subheader("Ringkasan semua kolom numerik")
    st.dataframe(df_f[kolom_numerik].describe().round(2), width="stretch")

# --------------------------- TAB VISUALISASI --------------------------
with tab_vis:
    kiri, kanan = st.columns(2)

    with kiri:
        st.subheader("Histogram")
        n_bins = st.slider("Jumlah bin", 5, 30, 10)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.hist(x, bins=n_bins, edgecolor="black")
        ax.axvline(stat["mean"], color="red", linestyle="--", label=f"Mean = {stat['mean']:.1f}")
        ax.axvline(stat["median"], color="green", label=f"Median = {stat['median']:.1f}")
        ax.set_xlabel(kolom)
        ax.set_ylabel("Frekuensi")
        ax.legend()
        st.pyplot(fig)

    with kanan:
        st.subheader("Boxplot")
        opsi_grup = ["(tanpa pengelompokan)"] + kolom_kategori
        grup = st.selectbox("Kelompokkan berdasarkan", opsi_grup)
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        if grup == opsi_grup[0]:
            ax2.boxplot(x)
            ax2.set_xticks([1])
            ax2.set_xticklabels([kolom])
        else:
            label, data = [], []
            for nama_grup, isi in df_f.groupby(grup):
                nilai = isi[kolom].dropna()
                if len(nilai) > 0:
                    label.append(str(nama_grup))
                    data.append(nilai)
            ax2.boxplot(data)
            ax2.set_xticks(range(1, len(label) + 1))
            ax2.set_xticklabels(label)
            ax2.set_xlabel(grup)
        ax2.set_ylabel(kolom)
        st.pyplot(fig2)

    st.caption("Tip: bandingkan posisi garis mean dan median pada histogram dengan bentuk boxplot.")

# ---------------------------- TAB DADU --------------------------------
with tab_dadu:
    st.subheader("Simulasi Lempar Dadu: Hukum Bilangan Besar")
    st.write(
        "Peluang teori tiap sisi dadu adalah 1/6 ≈ 0,167. "
        "Coba ubah jumlah lemparan dan lihat apakah proporsi hasil makin mendekati peluang teori."
    )

    n_lempar = st.slider("Jumlah lemparan", 10, 100000, 100, step=10)

    if st.button("🎲 Lempar dadu!"):
        st.session_state["hasil_dadu"] = np.random.randint(1, 7, size=n_lempar)

    hasil = st.session_state.get("hasil_dadu")
    if hasil is None:
        st.info("Tekan tombol **Lempar dadu!** untuk memulai simulasi.")
    else:
        frek = np.bincount(hasil, minlength=7)[1:]       # frekuensi sisi 1..6
        proporsi = frek / len(hasil)
        penyimpangan = np.abs(proporsi - 1 / 6).max()

        m1, m2 = st.columns(2)
        m1.metric("Total lemparan", f"{len(hasil):,}")
        m2.metric("Penyimpangan terbesar dari 1/6", f"{penyimpangan:.4f}")

        fig3, ax3 = plt.subplots(figsize=(7, 3.5))
        ax3.bar(range(1, 7), proporsi)
        ax3.axhline(1 / 6, color="red", linestyle="--", label="Peluang teori (1/6)")
        ax3.set_xlabel("Sisi dadu")
        ax3.set_ylabel("Proporsi")
        ax3.set_ylim(0, max(0.35, proporsi.max() * 1.15))
        ax3.legend()
        st.pyplot(fig3)

        tabel = pd.DataFrame({
            "Sisi": range(1, 7),
            "Frekuensi": frek,
            "Proporsi": proporsi.round(4),
        })
        st.dataframe(tabel, hide_index=True)

st.divider()
st.caption("Statistik dan Probabilitas 1 - Pertemuan 4")
