#Poin/Syarat G: Modul/Import - Minggu 7 & 10)
import streamlit as st
import datetime

#==========================================
#Poin/Syarat A: Tipe Data dan Variabel (String & Integer)
#==========================================
judul_aplikasi = "HealthWeb - Diagnosa Pencernaan"
ikon_aplikasi = "🏥"
batas_usia_minimal = 0

st.set_page_config(page_title=judul_aplikasi, page_icon=ikon_aplikasi, layout="centered")

#==========================================
#Poin/Syarat B: String (.format()) & Operator (Minggu 3)
#==========================================
tanggal_hari_ini = datetime.date.today().strftime('%d %B %Y')
teks_status_aktif = "Sistem aktif • Hari ini: **{}**".format(tanggal_hari_ini)

st.title("🏥 HealthWeb: Skrining Gangguan Pencernaan")
st.write(teks_status_aktif)
st.write("---")

#==========================================
#Poin/Syarat C: Percabangan if, elif, else (Minggu 4)
#==========================================
jam_sekarang = datetime.datetime.now().hour
if jam_sekarang < 11:
    sapaan_waktu = "Selamat Pagi"
elif jam_sekarang < 15:
    sapaan_waktu = "Selamat Siang"
elif jam_sekarang < 18:
    sapaan_waktu = "Selamat Sore"
else:
    sapaan_waktu = "Selamat Malam"

#==========================================
#Poin/Syarat D: Perulangan for (Minggu 5)
#==========================================
kumpulan_tips = [
    "🧼 **Jaga Kebersihan**\n\nCuci tangan sebelum makan dan pastikan makanan serta air minum dimasak hingga matang.",
    "🥦 **Cukupi Serat & Air**\n\nKonsumsi sayur, buah, dan air putih minimal 2 liter sehari untuk melancarkan pencernaan.",
    "⏱️ **Jangan Tunda BAB**\n\nSegera buang air besar saat terasa mulas dan hindari mengejan terlalu keras."
]

hasil_format_tips = []
for idx in range(len(kumpulan_tips)):
    hasil_format_tips.append(kumpulan_tips[idx])

#==========================================
#Poin/Syarat E: Tuple & List (Minggu 6)
#==========================================
PILIHAN_MENU = ("🏠 Beranda & Tips Pencernaan", "🏥 Cek Gejala Pencernaan")

DAFTAR_GEJALA = [
    "BAB Cair / Mencret Lebih dari 3 Kali Sehari",
    "BAB Berdarah Segar & Nyeri/Benjolan di Anus",
    "Diare Kronis Berdarah/Berlendir & Berat Badan Turun",
    "Nyeri Tajam di Perut Kanan Bawah (Makin Sakit Saat Bergerak)",
    "Muntah-Muntah Disertai Diare Cair Mendadak",
    "Demam Tinggi Naik Bertahap (Sore/Malam) & Sakit Kepala"
]

#==========================================
#Poin/Syarat F: Fungsi (Minggu 9)
#==========================================
def diagnosa_penyakit(gejala):
    """Fungsi untuk menganalisis 1 gejala utama pasien dan mengembalikan diagnosa."""
    if gejala == "BAB Cair / Mencret Lebih dari 3 Kali Sehari":
        return (
            "Terdeteksi Kemungkinan Diare. "
            "Segera minum larutan oralit atau air putih yang banyak untuk mencegah dehidrasi, "
            "konsumsi makanan lunak rendah serat (seperti bubur atau pisang), dan hindari makanan pedas, berminyak, serta produk susu."
        )
    elif gejala == "BAB Berdarah Segar & Nyeri/Benjolan di Anus":
        return (
            "Terdeteksi Kemungkinan Ambeien (Wasir). "
            "Perbanyak konsumsi makanan tinggi serat (sayur dan buah) serta air putih agar feses lunak, "
            "hindari mengejan terlalu keras atau duduk terlalu lama di toilet, dan rendam area anus dengan air hangat (sitz bath) untuk meredakan nyeri."
        )
    elif gejala == "Diare Kronis Berdarah/Berlendir & Berat Badan Turun":
        return (
            "Terdeteksi Kemungkinan Penyakit Radang Usus (IBD). "
            "Kondisi ini memerlukan pemeriksaan medis lanjutan oleh dokter spesialis penyakit dalam. "
            "Catat frekuensi BAB Anda, jaga asupan cairan, hindari makanan pemicu iritasi usus, dan segera periksakan diri ke fasilitas kesehatan."
        )
    elif gejala == "Nyeri Tajam di Perut Kanan Bawah (Makin Sakit Saat Bergerak)":
        return (
            "Terdeteksi Kemungkinan Usus Buntu (Apendisitis) — [Peringatan Darurat]. "
            "SEGERA pergi ke IGD rumah sakit terdekat untuk pemeriksaan dokter. "
            "Jangan mengonsumsi obat pereda nyeri, obat pencahar, atau mengompres hangat area perut sebelum diperiksa dokter karena berisiko memperparah peradangan."
        )
    elif gejala == "Muntah-Muntah Disertai Diare Cair Mendadak":
        return (
            "Terdeteksi Kemungkinan Muntaber (Gastroenteritis). "
            "Fokus utama adalah mencegah dehidrasi dengan meminum oralit atau air putih sedikit demi sedikit tetapi sering. "
            "Istirahatkan tubuh Anda dan hindari makanan padat yang berat hingga muntah mereda."
        )
    elif gejala == "Demam Tinggi Naik Bertahap (Sore/Malam) & Sakit Kepala":
        return (
            "Terdeteksi Kemungkinan Tifus (Demam Tifoid). "
            "Istirahat total (bed rest), perbanyak minum air putih, konsumsi makanan bertekstur lembut yang mudah dicerna, "
            "dan segera periksakan diri ke dokter untuk pemeriksaan darah serta pengobatan yang tepat."
        )
    else:
        return "Gejala belum dipilih atau belum spesifik."

#==========================================
#Navigasi Sidebar & Tampilan Halaman
#==========================================
with st.sidebar:
    st.subheader("🩺 Navigasi Sistem")
    st.write("---")
    menu_terpilih = st.radio("Silakan pilih halaman menu:", PILIHAN_MENU)
    st.write("---")
    with st.container():
        st.markdown("### 📊 Status Sistem")
        st.info("🟢 Server: **Online**\n\n🩺 Fokus: **Kesehatan Pencernaan**")
    st.write("")
    st.caption("HealthWeb • Universitas Bina Sarana Informatika")

#Halaman 1: BERANDA & TIPS PENCERNAAN
if menu_terpilih == "🏠 Beranda & Tips Pencernaan":
    st.subheader("{}, Selamat Datang di HealthWeb".format(sapaan_waktu))
    st.write("Aplikasi web ini dirancang untuk membantu Anda melakukan **skrining awal secara mandiri** terhadap gangguan saluran pencernaan berdasarkan keluhan utama yang dirasakan.")
    
    st.markdown("### 💡 Tips Menjaga Kesehatan Pencernaan:")
    kolom_tips = st.columns(3)
    for idx in range(len(hasil_format_tips)):
        with kolom_tips[idx]:
            st.info(hasil_format_tips[idx])

    st.markdown("### 📋 Cakupan Gejala yang Dapat Dideteksi:")
    for i in range(len(DAFTAR_GEJALA)):
        st.write("{}. {}".format(i + 1, DAFTAR_GEJALA[i]))

#Halaman 2: Cek Gejala Pencernaan Mandiri
elif menu_terpilih == "🏥 Cek Gejala Pencernaan":
    st.subheader("📋 Formulir Pemeriksaan Gejala")
    
    #==========================================
    #Poin/Syarat G: Modul & Eksepsi try - except & raise (Minggu 7 & 10)
    #==========================================
    try:
        nama_input = st.text_input("Masukkan Nama Lengkap Anda:", placeholder="Contoh: Bembi Satrio Archiputra")
        usia_input = st.text_input("Masukkan Usia Anda (Tahun):", placeholder="Contoh: 20")
        
        nama = nama_input.strip().title()
        
        if usia_input.strip():
            try:
                usia = int(usia_input.strip())
            except ValueError:
                raise ValueError("Usia harus berupa angka bulat, bukan huruf atau simbol!")
                
            if usia <= batas_usia_minimal:
                raise ValueError("Usia harus lebih dari 0 tahun!")
                
    except ValueError as ve:
        st.error("❌ Peringatan Input Usia: {}".format(ve))
        st.stop()

    if nama and usia_input.strip():
        tahun_sekarang = datetime.date.today().year
        perkiraan_lahir = tahun_sekarang - usia
        
        st.success("📋 Pasien Terdata: **{}** ({} Tahun • Lahir: {})".format(nama, usia, perkiraan_lahir))
        st.write("Silakan pilih **satu gejala utama** yang paling dominan Anda rasakan:")
        
        gejala_dipilih = st.selectbox(
            "Pilih gejala utama:",
            DAFTAR_GEJALA,
            index=None,
            placeholder="-- Klik untuk memilih satu gejala --"
        )
        
        st.write("")
        if st.button("🚀 Proses Analisis Gejala", use_container_width=True):
            if gejala_dipilih is None:
                st.warning("⚠️ Silakan pilih satu gejala terlebih dahulu sebelum menekan tombol proses.")
            else:
                st.write("---")
                st.subheader("🩺 Hasil Analisis Medis Sementara")

                hasil_medis = diagnosa_penyakit(gejala_dipilih)

                if "Peringatan Darurat" in hasil_medis:
                    st.error("🚨 {}".format(hasil_medis))
                else:
                    st.success("Rekomendasi Sistem: {}".format(hasil_medis))

                st.caption("Disclaimer: Aplikasi ini hanyalah sistem deteksi awal dan tidak menggantikan diagnosis dokter. Segera kunjungi fasilitas kesehatan terdekat jika keluhan/kondisi memburuk.")