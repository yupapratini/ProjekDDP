import streamlit as st
from jadwal import jadwal_pengumpulan
from laporan_sampah import tambah_laporan, tampilkan_laporan
from pencarian_tps import TPSLocator

# Custom CSS untuk tampilan
st.markdown(
    """
    <style>
    /* Warna latar belakang aplikasi */
    .stApp {
        background-color: #fffff;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #5f6f52;
        color: white;
        padding: 5px;
    }
    /* Teks pada sidebar */
    [data-testid="stSidebar"] * {
        color: black !important;
        font-size: 11px;
        margin-bottom: 5px;
        margin-top: 5px;
    }
    [data-testid="stSidebar"] *:hover {
        color: #ecf0f1 !important;
    }
    /* Header bar styling */
    header[data-testid="stHeader"] {
        background-color: #A9B388;
        color: white;
        padding: 5px;
        
    }
    header[data-testid="stHeader"] h1 {
        color: white;
        font-size: 10px;
    }
    .stButton > button:hover {
        background-color: #2980b9;
        color: #ecf0f1;
    }
    /* Custom title style for Panduan Daur Ulang */
    .sidebar-title {
        font-size: 20px;
        font-weight: bold;
        color: #ffffff;
        margin-bottom: 20px;
        text-align: center;
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app
tps_locator = TPSLocator()


st.title("Aplikasi Pengelolaan Sampah")
st.image("daur ulang.jpg")
menu = st.sidebar.selectbox("Pilih Menu", ["Beranda","Panduan Daur Ulang","Pengingat Jadwal","Pencarian TPS","Laporan Sampah"])

if menu == "Beranda":
    st.header("🏠Selamat Datang di Aplikasi Pengelolaan Sampah")
    st.write("Aplikasi ini dirancang untuk membantu Anda mengelola sampah dengan lebih baik.")
    st.write("Fitur yang tersedia:")
    st.markdown("""
    - *Pencarian TPS*: Cari alamat tempat pembuangan sampah berdasarkan kota.
    - *Pengingat Jadwal*: Atur pengingat untuk pengumpulan sampah sesuai jadwal Anda.
    - *Laporan Sampah*: Tambahkan dan lihat laporan sampah yang telah Anda buang.
    - *Panduan Daur Ulang*: Pelajari cara mendaur ulang berbagai jenis sampah.
    """)
    st.write("Gunakan menu di sebelah kiri untuk mulai menjelajahi fitur aplikasi.")
    
elif menu == "Panduan Daur Ulang":
    st.header("♻️ Panduan Daur Ulang")
    st.write("Pelajari cara mendaur ulang berbagai jenis sampah dengan benar:")
    st.markdown("""
    ### Panduan:
    - *Plastik*:
        - Cuci bersih plastik sebelum didaur ulang.
        - Pisahkan plastik keras (seperti botol) dan plastik lunak (seperti kantong plastik).
    - *Kertas*:
        - Hindari mencampur kertas yang berminyak atau basah.
        - Lipat atau gulung kertas agar lebih mudah disimpan.
    - *Kaca*:
        - Pisahkan kaca dari material lainnya.
        - Pastikan kaca tidak pecah atau tajam sebelum dikirim ke tempat daur ulang.
    - *Logam*:
        - Cuci kaleng atau material logam sebelum diserahkan ke tempat daur ulang.
        - Hindari mencampur logam dengan material lain.
    - *Sampah Organik*:
        - Gunakan sampah organik untuk membuat kompos.
        - Pisahkan sampah organik dari material non-organik.
    """)
    st.write("Dengan mengikuti panduan ini, Anda dapat membantu menjaga lingkungan dan mendukung keberlanjutan.")

elif menu == "Pengingat Jadwal":
    st.header("🗓️Pengingat Jadwal Pengumpulan Sampah")
    hari_input = st.selectbox("Pilih hari:", ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"])
    waktu_input = st.text_input("Masukkan waktu pengumpulan (HH:MM):", "07:00")
    
    if st.button("Setel Pengingat"):
        try:
            jadwal_pengumpulan(hari_input, waktu_input, lambda: st.write("Waktunya mengumpulkan sampah!"))
            st.success(f"Pengingat dijadwalkan untuk {hari_input} pukul {waktu_input}.")
        except ValueError as e:
            st.error(str(e))

elif menu == "Pencarian TPS":
    class TPSLocator:
        def _init_(self):
            self.data = {
                "bogor": "Jl. Raya Bogor KM.43, Bogor",
                "jakarta": "Jl. Daan Mogot KM.14, Jakarta Barat",
                "depok": "Jl. Raya Sawangan No.45, Depok",
                "tangerang": "Jl. Imam Bonjol No.89, Tangerang",
                "bekasi": "Jl. Narogong KM.13, Bekasi",
                "bandung": "Jl. Babakan Siliwangi No.15, Bandung"
            }
        
        def cari_tps(self, kota):
            if kota in self.data:
                return self.data[kota]
            else:
                return "Alamat TPS tidak ditemukan untuk kota ini."

    st.header("📍 Pencarian Alamat TPS")
    st.write("""
             alamat yang bisa di cari:
                - *Bogor*
                - *Jakarta*
                - *Depok*
                - *Tangerang*
                - *Bekasi*
                - *Bandung*
             """)
    kota_input = st.text_input("Masukkan nama kota untuk mencari alamat TPS:")
    if st.button("Cari Alamat TPS"):
        hasil = tps_locator.cari_tps(kota_input)
        st.write(hasil)

elif menu == "Laporan Sampah":
    st.header("📊 Laporan Sampah Harian")
    tampilkan_laporan()