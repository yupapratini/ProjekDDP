import streamlit as st
import pandas as pd

if "data_laporan" not in st.session_state:
    st.session_state["data_laporan"] = []

def tambah_laporan(tanggal, jenis, jumlah):
    st.session_state["data_laporan"].append({
        "Tanggal": tanggal,
        "Jenis Sampah": jenis,
        "Jumlah (kg)": jumlah
    })

def tampilkan_laporan():
   
    if "data_laporan" not in st.session_state:
        st.session_state["data_laporan"] = []

    tanggal = st.date_input("Pilih tanggal:")
    jenis = st.selectbox("Pilih jenis sampah:", ["Organik", "Anorganik", "B3", "Lainnya"])
    jumlah = st.number_input("Masukkan jumlah sampah (kg):", min_value=1, step=1)
    
    if st.button("Tambah Laporan"):
        tambah_laporan(tanggal.strftime("%Y-%m-%d"), jenis, int(jumlah))
        st.success("Laporan berhasil ditambahkan!")
    
    st.header("Daftar Laporan Sampah")
    if st.session_state["data_laporan"]:
        df = pd.DataFrame(st.session_state["data_laporan"])
        st.table(df)
    else:
        st.write("Belum ada laporan sampah yang ditambahkan.")
