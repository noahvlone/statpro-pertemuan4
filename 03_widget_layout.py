import streamlit as st

st.title("Widget dan Layout")

# ---------- Sidebar: tempat widget input ----------
st.sidebar.header("Pengaturan")
nama = st.sidebar.text_input("Nama", "Mahasiswa")
semester = st.sidebar.selectbox("Semester", [1, 2, 3, 4, 5, 6, 7, 8], index=2)
minat = st.sidebar.multiselect(
    "Minat",
    ["Statistika", "Machine Learning", "Visualisasi", "Basis Data"],
    default=["Statistika"],
)
jumlah = st.sidebar.slider("Jumlah data", 10, 100, 30)
detail = st.sidebar.checkbox("Tampilkan detail", value=True)

st.write(f"Halo **{nama}** (semester {semester})")

# ---------- Columns: tata letak berdampingan ----------
kol1, kol2, kol3 = st.columns(3)
kol1.metric("Semester", semester)
kol2.metric("Jumlah minat", len(minat))
kol3.metric("Jumlah data", jumlah)

# ---------- Tabs: pindah tampilan tanpa pindah halaman ----------
tab1, tab2 = st.tabs(["Detail", "Tombol"])

with tab1:
    if detail:
        st.write("Minat kamu:", minat)
    else:
        st.info("Centang 'Tampilkan detail' di sidebar.")

with tab2:
    if st.button("Klik aku!"):
        st.balloons()
        st.write("Tombol ditekan 🎉")

# ---------- Eksperimen: Streamlit menjalankan ulang seluruh skrip ----------
st.divider()
st.subheader("Eksperimen: skrip dijalankan ulang setiap interaksi")

hitung = 0
if st.button("Tambah (variabel biasa)"):
    hitung += 1
st.write("Variabel biasa:", hitung)

if "klik" not in st.session_state:
    st.session_state["klik"] = 0
if st.button("Tambah (session_state)"):
    st.session_state["klik"] += 1
st.write("session_state:", st.session_state["klik"])
