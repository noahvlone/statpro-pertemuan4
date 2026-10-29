from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard Kafe", page_icon="☕", layout="wide")

df = pd.read_csv(Path(__file__).parent / "data" / "data_penjualan_kafe.csv")

st.title("☕ Dashboard Penjualan Kafe")


def hitung_outlier(x):
    """Kembalikan nilai outlier (aturan 1,5 x IQR) dari sebuah Series."""
    # TODO 1: lengkapi fungsi ini
    pass


# TODO 2: di sidebar, buat multiselect "Menu" (default: semua menu),
#         lalu filter df sehingga hanya berisi menu yang dipilih (simpan di df_f).

# TODO 3: tampilkan 4 st.metric dalam 4 kolom:
#         (a) Total Pendapatan  (format: Rp1.234.567)
#         (b) Rata-rata Pendapatan Harian (total semua menu per tanggal, lalu di-mean)
#         (c) Tanggal dengan pendapatan harian tertinggi
#         (d) Jumlah outlier pada kolom Pendapatan (dideteksi PER MENU, lalu dijumlahkan)

# TODO 4: tampilkan grafik garis (st.line_chart) pendapatan harian total (index = Tanggal).

# TODO 5: buat boxplot Pendapatan per Menu (matplotlib + st.pyplot).

# TODO 6: tampilkan st.info(...) berisi kesimpulan singkat: menu mana yang punya outlier?

# TODO 7 (konseptual, tulis jawabanmu sebagai komentar di sini):
#         Coba hitung outlier pada kolom Pendapatan dengan SELURUH menu digabung (tanpa dipisah per menu).
#         Apakah lonjakan penjualan Es Teh terdeteksi? Mengapa hasilnya berbeda dengan deteksi per menu?
