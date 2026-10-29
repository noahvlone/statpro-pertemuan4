import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("Tur Elemen Streamlit")

# ---------- 1. Teks ----------
st.header("1. Elemen Teks")
st.subheader("Ini subheader")
st.markdown("Teks **tebal**, *miring*, dan `kode`.")
st.caption("Caption: teks kecil untuk keterangan.")
st.latex(r"\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i")
st.code("rata_rata = sum(data) / len(data)", language="python")

# ---------- 2. Tampilan data ----------
st.header("2. Tampilan Data")
df = pd.DataFrame({
    "Nama": ["Andi", "Budi", "Citra", "Dewi"],
    "UTS": [78, 65, 88, 92],
})

st.dataframe(df)            # tabel interaktif (bisa di-sort)
st.table(df.head(2))        # tabel statis
st.metric(label="Rata-rata UTS", value=f"{df['UTS'].mean():.1f}", delta="+2.5")

# ---------- 3. Grafik ----------
st.header("3. Grafik Matplotlib")
fig, ax = plt.subplots(figsize=(5, 3))
ax.bar(df["Nama"], df["UTS"])
ax.set_ylabel("Nilai UTS")
ax.set_title("Nilai UTS per Mahasiswa")
st.pyplot(fig)
