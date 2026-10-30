PERTEMUAN 4 - Dashboard Statistik Deskriptif dengan Streamlit
===============================================================

STRUKTUR
  Pert4_Modul_Streamlit.ipynb      Modul/materi (penjelasan + sel %%writefile)
  Pert4_Gambaran_Dashboard_Streamlit.pptx   Slide gambaran (14 slide, ada speaker notes)
  app.py                           Dashboard final (4 tab) - referensi/demo pengajar
  01_hello.py ... 04_statistik.py  File langkah demi langkah (juga dibuat oleh notebook)
  kuis1.py, kuis2.py               Kerangka kuis untuk mahasiswa (ada TODO)
  data/data_mahasiswa.csv          Dataset demo dashboard (60 mahasiswa)
  data/data_penjualan_kafe.csv     Dataset kuis 2 (30 hari x 3 menu)

CARA PAKAI
  1) pip install -U streamlit pandas numpy matplotlib
  2) Buka terminal di folder ini, lalu:  streamlit run app.py
     (jika perintah tidak dikenali:     python -m streamlit run app.py)
  3) Notebook dijalankan di Jupyter/VS Code (bukan Colab) hanya untuk MENULIS file .py;
     aplikasinya tetap dijalankan dari terminal.

CATATAN UNTUK MAHASISWA
  Bagikan: notebook, folder data/, kuis1.py, kuis2.py (opsional: pptx).
  Jangan bagikan: kunci_kuis1.py, kunci_kuis2.py.
