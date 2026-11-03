# ==========================================
# Poin/Syarat G: Modul/Import Library 
# ==========================================
import streamlit as st
import datetime

# Poin/Syarat F: Tuple/Menu Navigasi 
PILIHAN_MENU = ("🏠 Beranda & Tips", "🏥 Cek Gejala Mandiri")

# ==========================================
# Fungsi Logika Medis
# ==========================================
def diagnosa_penyakit(gejala_list):
    # Tempat menampung semua rekomendasi yang cocok
    semua_rekomendasi = []
    
    # =========================================================================
    # Poin/Syarat C: Logika Gabungan Penyakit (Diperiksa paling awal)
    # =========================================================================
    if "Demam" in gejala_list and "Batuk" in gejala_list and "Pilek" in gejala_list:
        semua_rekomendasi.append("Indikasi Influenza (Flu). Optimalkan proses pemulihan dengan istirahat yang cukup, perbanyak minum air hangat untuk meredakan tenggorokan, dan konsumsi suplemen Vitamin C. Batasi interaksi langsung dengan orang lain sementara waktu untuk mencegah penularan.")
    
    elif "Demam" in gejala_list and "Pusing" in gejala_list and "Mual/Muntah" in gejala_list:
        semua_rekomendasi.append("Indikasi gejala awal Demam Berdarah (DBD) atau Typhus. Disarankan untuk memantau suhu tubuh secara berkala, menjaga asupan cairan dengan minum air putih guna mencegah dehidrasi, dan istirahat total. Segera lakukan pemeriksaan darah di klinik atau laboratorium terdekat jika gejala menetap atau memburuk dalam waktu lebih dari 3 hari.")
    
    elif "Batuk" in gejala_list and "Sesak Napas" in gejala_list:
        semua_rekomendasi.append("Indikasi Gangguan Saluran Pernapasan (seperti Bronkitis atau Asma). Disarankan untuk menghindari paparan polusi, asap rokok, dan debu secara ketat, serta selalu menggunakan masker saat beraktivitas. Jaga sirkulasi udara di dalam ruangan tetap bersih dan segera konsultasikan ke dokter spesialis paru jika sesak napas terasa semakin berat.")
    
    # =========================================================================
    # Poin/Syarat C: Logika Gejala Satu per satu (Menggunakan 'if' terpisah agar bisa dobel)
    # Jika sudah masuk ke logika gabungan di atas, gejala tunggal di bawah ini dilewati demi akurasi.
    # =========================================================================
    if not semua_rekomendasi:
        if "Demam" in gejala_list:
            semua_rekomendasi.append("Terdeteksi gejala Demam. Kondisi ini umumnya merupakan respons tubuh dalam melawan infeksi. Disarankan untuk memantau suhu tubuh secara berkala dengan termometer, perbanyak minum air putih, dan kompres air hangat jika diperlukan.")
            
        if "Sesak Napas" in gejala_list:
            semua_rekomendasi.append("Terdeteksi gejala Sesak Napas. Ini merupakan gejala yang memerlukan perhatian khusus. Istirahatlah dalam posisi duduk tegak di ruangan dengan sirkulasi udara yang baik. Jika sesak semakin parah, segera cari bantuan medis.")
            
        if "Batuk" in gejala_list:
            semua_rekomendasi.append("Terdeteksi gejala Batuk. Hindari konsumsi makanan berminyak, es, atau makanan pedas yang dapat memicu iritasi tenggorokan. Perbanyak minum air hangat atau madu untuk meredakan tenggorokan Anda.")
            
        if "Pilek" in gejala_list:
            semua_rekomendasi.append("Terdeteksi gejala Pilek. Jaga tubuh agar tetap hangat, hirup uap air hangat jika hidung terasa tersumbat, dan gunakan tisu bersih atau masker untuk mencegah penyebaran virus ke sekitar Anda.")
            
        if "Pusing" in gejala_list:
            semua_rekomendasi.append("Terdeteksi gejala Pusing. Segera istirahatkan tubuh dengan berbaring di tempat yang tenang dan redup. Hindari gerakan kepala secara tiba-tiba dan pastikan Anda sudah makan secara teratur.")
            
        if "Mual/Muntah" in gejala_list:
            semua_rekomendasi.append("Terdeteksi gejala Mual/Muntah. Untuk sementara, hindari makanan yang berbau tajam, berlemak, atau terlalu manis. Konsumsi makanan dalam porsi kecil tetapi sering, serta minum air sedikit demi sedikit agar tidak dehidrasi.")
            
    # =========================================================================
    # Poin/Syarat C: Kondisi Cadangan (jika list masih kosong / tidak ada yang dicentang)
    # =========================================================================
    if not semua_rekomendasi:
        semua_rekomendasi.append("Gejala terlalu umum atau tidak spesifik. Jaga imunitas tubuh Anda dengan makan bergizi, olahraga ringan, dan minum vitamin.")
        
    return semua_rekomendasi

    
# ==========================================
# Tampilan Web
# ==========================================
# Poin/Syarat B: String dan Operator 
st.set_page_config(page_title="HealthWeb - Diagnosa Mandiri", page_icon="🏥", layout="centered")

# --- Kustomisasi Font (Masukan/Pengubahan supaya lebih bagus)
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        /* Mengubah font */
        html, body, [class*="css"], .stApp {
            font-family: 'Plus Jakarta Sans', sans-serif;
        }
        
        /* Memperbagus tampilan judul */
        h1 {
            font-weight: 700 !important;
            color: #1E3A8A !important;
        }
        h2, h3 {
            font-weight: 600 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Konten Utama
st.title("🏥 HealthWeb: Aplikasi Diagnosa Kesehatan")
st.write(f"Sistem aktif • Hari ini: **{datetime.date.today().strftime('%d %B %Y')}**")
st.write("---")

# --- Modifikasi Sidebar lebih berisi/tidak polos ---
with st.sidebar:
    # Header & Visual tambahan di atas agar tidak sepi
    st.markdown("<h2 style='text-align: center; font-size: 50px; margin-bottom: 0px;'>🩺</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; margin-top: 0px;'>Navigasi Sistem</h3>", unsafe_allow_html=True)
    st.write("---")
    
    # Widget Navigasi Utama
    menu_terpilih = st.radio("Silakan pilih halaman menu:", PILIHAN_MENU)
    
    st.write("---")
    # Informasi tambahan di bawah agar mengisi ruang kosong
    with st.container():
        st.markdown("### 📊 Status Sistem")
        st.info("🟢 Server: **Online**\n\n📌 Versi: **v1.2.0**")
    
    # Footer kecil di bagian paling bawah sidebar
    st.markdown("<br><br><br><p style='text-align: center; color: gray; font-size: 11px;'> HealthWeb_Universitas Bina Sarana Informatika </p>", unsafe_allow_html=True)


# ------------------------------------------
# Halaman 1: BERANDA & TIPS
# ------------------------------------------
if menu_terpilih == "🏠 Beranda & Tips":
    st.subheader("Selamat Datang di HealthWeb")
    st.write("Aplikasi web ini dirancang untuk membantu Anda melakukan **skrining atau deteksi dini secara mandiri** terhadap gejala kesehatan yang sedang dirasakan.")
    
    st.markdown("### 💡 Tips Menjaga Imunitas Hari Ini:")
    
    # Desain Layout Kolom Berdampingan Tips Kesehatan
    kolom_tips1, kolom_tips2, kolom_tips3 = st.columns(3)
    
    with kolom_tips1:
        st.info("💧 **Hidrasi Cukup**\n\nMinum air putih minimal 8 gelas per hari untuk menjaga cairan tubuh.")
    with kolom_tips2:
        st.info("😴 **Istirahat Teratur**\n\nTidur berkualitas selama 7-8 jam setiap malam agar imun kuat.")
    with kolom_tips3:
        st.info("🧼 **Sanitasi Diri**\n\nRutin mencuci tangan menggunakan sabun sebelum dan sesudah beraktivitas.")

# ------------------------------------------
# Halaman 2: Cek Gejala secara Mandiri
# Poin/Syarat G: Eksepsi
# ------------------------------------------
elif menu_terpilih == "🏥 Cek Gejala Mandiri":
    st.subheader("📋 Formulir Pemeriksaan Gejala")
    
    # Validasi Input Usia/Umur
    try:
        # Poin/Syarat A: Tipe Data/Variabel
        nama = st.text_input("Masukkan Nama Lengkap Anda:", placeholder="Contoh: Bembi Satrio Archiputra")
        usia_input = st.text_input("Masukkan Usia Anda (Tahun):", placeholder="Contoh: 20")
        
        if usia_input:
            usia = int(usia_input) # Konversi ke integer buat validasi
    except ValueError:
        st.error("❌ Peringatan: Kolom usia wajib diisi menggunakan angka!")
        st.stop()

    if nama and usia_input:
        st.success(f"📋 Pasien Terdata: **{nama}** ({usia} Tahun)")
        st.write("Silakan pilih daftar gejala medis yang Anda rasakan saat ini:")
        
        # Poin/Syarat D dan E: Perulangan dan List
        daftar_opsi_gejala = ["Demam", "Batuk", "Pilek", "Pusing", "Mual/Muntah", "Sesak Napas"]
        
        # Widget multi-select interaktif bawaan Streamlit
        gejala_dipilih = st.multiselect("Pilih satu atau beberapa gejala:", daftar_opsi_gejala)
        
        # Poin/Syarat B: Operator (Desain layout tombol proses) 
        st.write("")
        if st.button("🚀 Proses Analisis Medis", use_container_width=True):
            if len(gejala_dipilih) == 0:
                st.warning("⚠️ Silakan pilih minimal satu gejala terlebih dahulu sebelum menekan tombol proses.")
            else:
                st.write("---")
                st.subheader("🩺 Hasil Analisis Medis Sementara")
                
                # Memanggil Fungsi Logika Medis (Sekarang menghasilkan sebuah LIST)
                daftar_hasil = diagnosa_penyakit(gejala_dipilih)
                
                # Menampilkan rekomendasi satu per satu dengan nomor
                for indeks, hasil in enumerate(daftar_hasil, start=1):
                    st.success(f"**Rekomendasi {indeks}:** {hasil}")
                
                # Disclaimer Medis
                st.caption("*Disclaimer: Aplikasi ini hanyalah sistem pakar deteksi awal. Jika kondisi fisik memburuk, segera hubungi dokter atau fasilitas kesehatan terdekat.*")
