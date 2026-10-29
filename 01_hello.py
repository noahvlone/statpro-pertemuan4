import streamlit as st

st.title("Hello, Streamlit! 👋")
st.write("Ini aplikasi web pertamaku, dibuat hanya dengan Python.")

nama = st.text_input("Siapa namamu?")

if nama:
    st.success(f"Halo, {nama}! Selamat datang di StatPro 1.")
