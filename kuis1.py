import numpy as np
import streamlit as st

st.title("🧮 Kalkulator Statistik Mini")
st.write("Masukkan angka-angka yang dipisah koma. Contoh: 70, 85, 90, 65, 78")

teks = st.text_input("Data angka")

# TODO 1: buat tombol "Hitung".
#         Semua langkah di bawah dikerjakan HANYA jika tombol ditekan.
# TODO 2: ubah teks menjadi list angka (float) dengan split(",").
#         Gunakan try-except: jika ada yang bukan angka, tampilkan st.error(...) lalu st.stop().
# TODO 3: jika angka kurang dari 2 buah, tampilkan st.warning(...) lalu st.stop().
# TODO 4: ubah ke np.array, lalu tampilkan Mean, Median, Std Dev (sampel, ddof=1),
#         Min, dan Max memakai st.metric di dalam 5 kolom (st.columns).
