from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

DATA_PATH = Path(__file__).parent / "data" / "data_mahasiswa.csv"


@st.cache_data          # data dibaca sekali saja, bukan setiap interaksi
def muat_data(path):
    return pd.read_csv(path)


df = muat_data(DATA_PATH)

st.title("Statistik Deskriptif Interaktif")

kolom = st.selectbox("Pilih kolom numerik", ["UTS", "UAS", "Jam_Belajar", "Kehadiran"])
x = df[kolom].dropna()          # buang data kosong

c1, c2, c3, c4 = st.columns(4)
c1.metric("Mean", f"{x.mean():.2f}")
c2.metric("Median", f"{x.median():.2f}")
c3.metric("Std Dev (sampel)", f"{x.std():.2f}")
c4.metric("Jumlah data (n)", len(x))

fig, ax = plt.subplots(figsize=(6, 3))
ax.hist(x, bins=10, edgecolor="black")
ax.axvline(x.mean(), color="red", linestyle="--", label="Mean")
ax.axvline(x.median(), color="green", label="Median")
ax.set_xlabel(kolom)
ax.set_ylabel("Frekuensi")
ax.legend()
st.pyplot(fig)
