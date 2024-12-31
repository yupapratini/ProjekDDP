import streamlit as st
import datetime
import threading
import time

def jadwal_pengumpulan(hari, waktu, callback):
    """
    Fungsi untuk membuat pengingat jadwal pengumpulan sampah.

    Args:
        hari (str): Nama hari dalam bahasa Indonesia (contoh: "senin", "selasa").
        waktu (str): Waktu dalam format HH:MM (contoh: "07:00").
        callback (function): Fungsi yang akan dijalankan saat waktu pengumpulan tiba.
    """
    hari_mapping = {
        "senin": 0,
        "selasa": 1,
        "rabu": 2,
        "kamis": 3,
        "jumat": 4,
        "sabtu": 5,
        "minggu": 6
    }

    if hari.lower() not in hari_mapping:
        raise ValueError("Hari tidak valid. Masukkan hari dalam bahasa Indonesia.")

    target_hari = hari_mapping[hari.lower()]
    target_waktu = datetime.datetime.strptime(waktu, "%H:%M").time()

    def cek_jadwal():
        while True:
            sekarang = datetime.datetime.now()
            hari_sekarang = sekarang.weekday()
            waktu_sekarang = sekarang.time()

            if hari_sekarang == target_hari and waktu_sekarang >= target_waktu:
                callback()
                break

            time.sleep(30)  # Cek setiap 30 detik

    threading.Thread(target=cek_jadwal).start()

def pengingat():
    st.write("Waktunya mengumpulkan sampah!")

# Streamlit app
st.title("Pengingat Jadwal Pengumpulan Sampah")

hari_input = st.selectbox("Pilih hari:", ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
waktu_input = st.text_input("Masukkan waktu pengumpulan (HH:MM):", "07:00")

if st.button("Setel Pengingat"):
    try:
        jadwal_pengumpulan(hari_input, waktu_input, pengingat)
        st.success(f"Pengingat dijadwalkan untuk {hari_input} pukul {waktu_input}.")
    except ValueError as e:
        st.error(str(e))
