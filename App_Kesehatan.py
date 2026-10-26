# ==========================================
# Modul/Import Library 
# ==========================================
import streamlit as st
import datetime

# TUPLE/Menu Navigasi 
PILIHAN_MENU = ("🏠 Beranda & Tips", "🏥 Cek Gejala Mandiri")

# ==========================================
# Fungsi Logika Medis
# ==========================================
def diagnosa_penyakit(gejala_list):
    # =========================================================================
    # 1. Logika Gabungan Penyakit 
    # =========================================================================
    if "Demam" in gejala_list and "Batuk" in gejala_list and "Pilek" in gejala_list:
        return "Indikasi Influenza (Flu). Optimalkan proses pemulihan dengan istirahat yang cukup, perbanyak minum air hangat untuk meredakan tenggorokan, dan konsumsi suplemen Vitamin C. Batasi interaksi langsung dengan orang lain sementara waktu untuk mencegah penularan."
    
    elif "Demam" in gejala_list and "Pusing" in gejala_list and "Mual/Muntah" in gejala_list:
        return "Indikasi gejala awal Demam Berdarah (DBD) atau Typhus. Disarankan untuk memantau suhu tubuh secara berkala, menjaga asupan cairan dengan minum air putih guna mencegah dehidrasi, dan istirahat total. Segera lakukan pemeriksaan darah di klinik atau laboratorium terdekat jika gejala menetap atau memburuk dalam waktu lebih dari 3 hari."
    
    elif "Batuk" in gejala_list and "Sesak Napas" in gejala_list:
        return "Indikasi Gangguan Saluran Pernapasan (seperti Bronkitis atau Asma). Disarankan untuk menghindari paparan polusi, asap rokok, dan debu secara ketat, serta selalu menggunakan masker saat beraktivitas. Jaga sirkulasi udara di dalam ruangan tetap bersih dan segera konsultasikan ke dokter spesialis paru jika sesak napas terasa semakin berat."
    
    # =========================================================================
    # 2. Logika Gejala Satu per satu (Misal tidak ada gabungan kaya diatas)
    # =========================================================================
    elif "Demam" in gejala_list:
        return "Terdeteksi gejala Demam. Kondisi ini umumnya merupakan respons tubuh dalam melawan infeksi. Disarankan untuk memantau suhu tubuh secara berkala dengan termometer, perbanyak minum air putih, dan kompres air hangat jika diperlukan."
        
    elif "Sesak Napas" in gejala_list:
        return "Terdeteksi gejala Sesak Napas. Ini merupakan gejala yang memerlukan perhatian khusus. Istirahatlah dalam posisi duduk tegak di ruangan dengan sirkulasi udara yang baik. Jika sesak semakin parah, segera cari bantuan medis."
        
    elif "Batuk" in gejala_list:
        return "Terdeteksi gejala Batuk. Hindari konsumsi makanan berminyak, es, atau makanan pedas yang dapat memicu iritasi tenggorokan. Perbanyak minum air hangat atau madu untuk meredakan tenggorokan Anda."
        
    elif "Pilek" in gejala_list:
        return "Terdeteksi gejala Pilek. Jaga tubuh agar tetap hangat, hirup uap air hangat jika hidung terasa tersumbat, dan gunakan tisu bersih atau masker untuk mencegah penyebaran virus ke sekitar Anda."
        
    elif "Pusing" in gejala_list:
        return "Terdeteksi gejala Pusing. Segera istirahatkan tubuh dengan berbaring di tempat yang tenang dan redup. Hindari gerakan kepala secara tiba-tiba dan pastikan Anda sudah makan secara teratur."
        
    elif "Mual/Muntah" in gejala_list:
        return "Terdeteksi gejala Mual/Muntah. Untuk sementara, hindari makanan yang berbau tajam, berlemak, atau terlalu manis. Konsumsi makanan dalam porsi kecil tetapi sering, serta minum air sedikit demi sedikit agar tidak dehidrasi."
        
    # =========================================================================
    # 3. Kondisi Cadangan (tidak ada yang dicentang)
    # =========================================================================
    else:
        return "Gejala terlalu umum atau tidak spesifik. Jaga imunitas tubuh Anda dengan makan bergizi, olahraga ringan, dan minum vitamin."
    
# ==========================================
# Tampilan Web
# ==========================================
# String dan Operator 
st.set_page_config(page_title="HealthWeb - Diagnosa Mandiri", page_icon="🏥", layout="centered")

st.title("🏥 HealthWeb: Aplikasi Diagnosa Kesehatan")
st.write(f"Sistem aktif • Hari ini: **{datetime.date.today().strftime('%d %B %Y')}**")
st.write("---")

# Navigasi Menu Sidebar/Disamping Kiri
st.sidebar.header("🕹️ Navigasi Sistem")
menu_terpilih = st.sidebar.radio("Pilih Halaman:", PILIHAN_MENU)

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
# Halaman 2: CEK GEJALA MANDIRI
# ------------------------------------------
elif menu_terpilih == "🏥 Cek Gejala Mandiri":
    st.subheader("📋 Formulir Pemeriksaan Gejala")
    
    # Validasi Input Usia/Umur
    try:
        # Data/Variabel
        nama = st.text_input("Masukkan Nama Lengkap Anda:", placeholder="Contoh: Bembi Suka Nasi Goreng")
        usia_input = st.text_input("Masukkan Usia Anda (Tahun):", placeholder="Contoh: 20")
        
        if usia_input:
            usia = int(usia_input) # Konversi ke integer buat validasi
    except ValueError:
        st.error("❌ Peringatan: Kolom usia wajib diisi menggunakan angka!")
        st.stop()

    if nama and usia_input:
        st.success(f"📋 Pasien Terdata: **{nama}** ({usia} Tahun)")
        st.write("Silakan pilih daftar gejala medis yang Anda rasakan saat ini:")
        
        # Perulangan dan List
        daftar_opsi_gejala = ["Demam", "Batuk", "Pilek", "Pusing", "Mual/Muntah", "Sesak Napas"]
        
        # Widget multi-select interaktif bawaan Streamlit
        gejala_dipilih = st.multiselect("Pilih satu atau beberapa gejala:", daftar_opsi_gejala)
        
        # Desain layout tombol proses 
        st.write("")
        if st.button("🚀 Proses Analisis Medis", use_container_width=True):
            if len(gejala_dipilih) == 0:
                st.warning("⚠️ Silakan pilih minimal satu gejala terlebih dahulu sebelum menekan tombol proses.")
            else:
                st.write("---")
                st.subheader("🩺 Hasil Analisis Medis Sementara")
                
                # Manggil Fungsi Logika Medis
                hasil_medis = diagnosa_penyakit(gejala_dipilih)
                
                # Tampilan output kotak hijau (Success)
                st.success(f"**Rekomendasi Sistem:** {hasil_medis}")
                
                # Disclaimer Medis Tambahan demi Keselamatan dan Laporan
                st.caption("*Disclaimer: Aplikasi ini hanyalah sistem pakar deteksi awal. Jika kondisi fisik memburuk, segera hubungi dokter atau fasilitas kesehatan terdekat.*")
