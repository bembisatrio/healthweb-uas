#==========================================
#Poin/Syarat G: Modul/Import Library 
#==========================================
import streamlit as st
import datetime

#Poin/Syarat F: Tuple/Menu Navigasi 
PILIHAN_MENU = ("🏠 Beranda & Tips Lambung", "🏥 Cek Gejala Lambung")

#==========================================
#Fungsi Logika Medis (Fokus Penyakit Lambung)
#==========================================
def diagnosa_penyakit(gejala_list):
    """Fungsi untuk menganalisis daftar gejala lambung pasien dan mengembalikan 1 rekomendasi medis utama."""
    
    # Menggunakan set agar pengecekan kombinasi gejala lebih rapi dan cepat
    gejala = set(gejala_list)
    
    #=========================================================================
    #1. Logika Gabungan 3 Gejala (Prioritas Tertinggi)
    #=========================================================================
    if {"Nyeri Ulu Hati", "Mual/Muntah", "Perut Kembung/Begah"}.issubset(gejala):
        return (
            "Indikasi Gastritis Akut (Radang Dinding Lambung) atau Maag Kronis. "
            "Dinding lambung Anda sedang mengalami iritasi atau peradangan. "
            "Konsumsi makanan bertekstur lunak dalam porsi kecil tetapi sering (seperti bubur), "
            "hindari total makanan pedas, asam, berlemak, serta minuman berkafein. "
            "Bila nyeri terasa menusuk hebat, segera periksakan diri ke fasilitas kesehatan."
        )

    elif {"Dada Terasa Panas (Heartburn)", "Mulut Terasa Asam/Pahit", "Mual/Muntah"}.issubset(gejala):
        return (
            "Indikasi GERD Berat dengan Iritasi Esofagus. "
            "Naiknya asam lambung disertai mual menandakan katup lambung sedang melemah dan mengiritasi kerongkongan. "
            "Hindari makan dalam porsi besar, jangan berbaring minimal 3 jam setelah makan, dan segera konsultasikan ke dokter untuk terapi penetral asam lambung."
        )

    #=========================================================================
    #2. Logika Gabungan 2 Gejala (Prioritas Menengah)
    #=========================================================================
    elif {"Dada Terasa Panas (Heartburn)", "Mulut Terasa Asam/Pahit"}.issubset(gejala):
        return (
            "Indikasi GERD (Gastroesophageal Reflux Disease). "
            "Asam lambung Anda naik hingga ke kerongkongan. "
            "Segera duduk tegak atau posisikan kepala lebih tinggi saat berbaring, minum air putih hangat secara perlahan, "
            "dan hindari langsung tidur setelah makan (beri jeda minimal 2-3 jam). "
            "Segera konsultasikan ke dokter jika sensasi terbakar di dada terus berlanjut."
        )
    
    elif {"Nyeri Ulu Hati", "Perut Kembung/Begah"}.issubset(gejala):
        return (
            "Indikasi Sindrom Dispepsia (Maag disertai Penumpukan Gas). "
            "Terjadi peningkatan asam lambung sekaligus perlambatan gerak saluran cerna. "
            "Makanlah dalam porsi kecil namun sering, hindari makanan berlemak, pedas, serta minuman bersoda atau berkafein. "
            "Kompres hangat pada perut bagian atas dapat membantu meredakan rasa nyeri dan begah."
        )

    elif {"Nyeri Ulu Hati", "Mual/Muntah"}.issubset(gejala):
        return (
            "Indikasi Iritasi Mukosa Lambung (Gastritis Ringan). "
            "Lapisan pelindung lambung mengalami peradangan akibat paparan asam berlebih. "
            "Konsumsi makanan lembut yang mudah dicerna seperti bubur atau pisang, minum air hangat sedikit demi sedikit, "
            "dan hindari membiarkan perut kosong terlalu lama."
        )

    elif {"Perut Kembung/Begah", "Sering Bersendawa"}.issubset(gejala):
        return (
            "Indikasi Dispepsia Fungsional (Penumpukan Gas Lambung). "
            "Sistem pencernaan Anda mengalami perlambatan pengosongan lambung dan penumpukan gas. "
            "Hindari minuman bersoda, sayuran penghasil gas (seperti kol dan sawi), serta makanlah secara perlahan. "
            "Kompres hangat pada area perut bagian atas dapat membantu meredakan rasa begah."
        )

    elif {"Dada Terasa Panas (Heartburn)", "Sering Bersendawa"}.issubset(gejala):
        return (
            "Indikasi Refluks Gas dan Asam Lambung. "
            "Tekanan gas yang tinggi di lambung ikut mendorong asam naik ke arah kerongkongan. "
            "Hindari pakaian ketat di area perut, jangan langsung membungkuk setelah makan, dan kurangi konsumsi kopi maupun makanan tinggi lemak."
        )

    #=========================================================================
    #3. Logika Gejala Tunggal Lambung (Jika tidak ada gabungan di atas)
    #=========================================================================
    elif "Nyeri Ulu Hati" in gejala:
        return (
            "Terdeteksi gejala Nyeri Ulu Hati (Epigastrium). "
            "Kondisi ini menandakan peningkatan asam lambung atau lambung yang kosong terlalu lama. "
            "Segera konsumsi makanan ringan yang netral seperti biskuit tawar atau nasi tim, dan hindari obat pereda nyeri tanpa resep dokter."
        )
        
    elif "Dada Terasa Panas (Heartburn)" in gejala:
        return (
            "Terdeteksi gejala Heartburn (Rasa Panas di Dada). "
            "Longgarkan pakaian di area pinggang dan dada, tetap dalam posisi tegak, "
            "serta minum air mineral suhu ruang untuk membantu membilas asam yang naik ke kerongkongan."
        )
        
    elif "Mual/Muntah" in gejala:
        return (
            "Terdeteksi gejala Mual/Muntah akibat iritasi lambung. "
            "Hindari makanan berbau menyengat dan berminyak. "
            "Minumlah air putih atau larutan elektrolit sedikit demi sedikit agar tubuh tidak mengalami dehidrasi."
        )
        
    elif "Perut Kembung/Begah" in gejala:
        return (
            "Terdeteksi gejala Perut Kembung dan Begah. "
            "Lakukan jalan kaki ringan selama 10-15 menit untuk membantu pergerakan gas di saluran cerna, "
            "serta hindari mengunyah permen karet atau makan terburu-buru."
        )
        
    elif "Mulut Terasa Asam/Pahit" in gejala:
        return (
            "Terdeteksi gejala Regurgitasi Asam (Mulut Asam/Pahit). "
            "Berkumurlah dengan air bersih, minum air hangat, dan hindari konsumsi cokelat, makanan berlemak tinggi, "
            "serta kopi yang dapat melemahkan katup kerongkongan."
        )
        
    elif "Sering Bersendawa" in gejala:
        return (
            "Terdeteksi gejala Sering Bersendawa akibat udara berlebih di lambung. "
            "Kurangi minuman berkarbonasi, makanlah dalam porsi kecil, dan hindari berbicara berlebihan saat sedang mengunyah makanan."
        )
        
    #=========================================================================
    #4. Kondisi Cadangan
    #=========================================================================
    else:
        return (
            "Gejala lambung belum spesifik. "
            "Tetap jaga pola makan teratur tepat waktu, perbanyak konsumsi air putih, dan kelola tingkat stres Anda."
        )

#==========================================
#Tampilan Web
#==========================================
#Poin/Syarat B: String dan Operator 
st.set_page_config(page_title="HealthWeb - Diagnosa Lambung", page_icon="🏥", layout="centered")

#Konten Utama
st.title("🏥 HealthWeb: Aplikasi Skrining Lambung")
st.write(f"Sistem aktif • Hari ini: **{datetime.date.today().strftime('%d %B %Y')}**")
st.write("---")

#Modifikasi Sidebar agar lebih berisi dan informatif
with st.sidebar:
    st.markdown("<h2 style='text-align: center; font-size: 50px; margin-bottom: 0px;'>🩺</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; margin-top: 0px;'>Navigasi Sistem</h3>", unsafe_allow_html=True)
    st.write("---")
    
    #Widget Navigasi Utama
    menu_terpilih = st.radio("Silakan pilih halaman menu:", PILIHAN_MENU)
    
    st.write("---")
    with st.container():
        st.markdown("### 📊 Status Sistem")
        st.info("🟢 Server: **Online**\n\n🩺 Fokus: **Kesehatan Lambung**")
    
    #Footer di bagian paling bawah sidebar
    st.markdown("<br><br><br><p style='text-align: center; color: #1B5E20; font-size: 11px;'>HealthWeb • Universitas Bina Sarana Informatika</p>", unsafe_allow_html=True)

#------------------------------------------
#Halaman 1: BERANDA & TIPS LAMBUNG
#------------------------------------------
if menu_terpilih == "🏠 Beranda & Tips Lambung":
    st.subheader("Selamat Datang di HealthWeb")
    st.write("Aplikasi web ini dirancang khusus untuk membantu Anda melakukan **skrining atau deteksi dini secara mandiri** terhadap gangguan asam lambung, maag, dan GERD.")
    
    st.markdown("### 💡 Tips Menjaga Kesehatan Lambung Hari Ini:")
    
    #Desain Layout Kolom Berdampingan Tips Kesehatan Lambung
    kolom_tips1, kolom_tips2, kolom_tips3 = st.columns(3)
    
    with kolom_tips1:
        st.info("🍽️ **Makan Teratur**\n\nMakanlah dalam porsi kecil namun sering, dan jangan menunda jam makan utama.")
    with kolom_tips2:
        st.info("🚫 **Hindari Pemicu**\n\nBatasi makanan pedas, asam, gorengan, kopi, dan minuman bersoda.")
    with kolom_tips3:
        st.info("🛌 **Atur Posisi Tidur**\n\nBeri jeda 2-3 jam setelah makan sebelum berbaring agar asam lambung tidak naik.")

#------------------------------------------
#Halaman 2: Cek Gejala Lambung Mandiri
#Poin/Syarat G: Eksepsi
#------------------------------------------
elif menu_terpilih == "🏥 Cek Gejala Lambung":
    st.subheader("📋 Formulir Pemeriksaan Gejala Lambung")
    
    #Validasi Input Usia/Umur
    try:
        #Poin/Syarat A: Tipe Data/Variabel
        nama = st.text_input("Masukkan Nama Lengkap Anda:", placeholder="Contoh: Bembi Satrio Archiputra")
        usia_input = st.text_input("Masukkan Usia Anda (Tahun):", placeholder="Contoh: 20")
        
        if usia_input:
            usia = int(usia_input)
    except ValueError:
        st.error("❌ Peringatan: Kolom usia wajib diisi menggunakan angka!")
        st.stop()

    if nama and usia_input:
        st.success(f"📋 Pasien Terdata: **{nama}** ({usia} Tahun)")
        st.write("Silakan pilih keluhan lambung yang sedang Anda rasakan saat ini:")
        
        #Poin/Syarat D dan E: Perulangan dan List
        daftar_opsi_gejala = [
            "Nyeri Ulu Hati",
            "Perut Kembung/Begah",
            "Mual/Muntah",
            "Dada Terasa Panas (Heartburn)",
            "Sering Bersendawa",
            "Mulut Terasa Asam/Pahit"
        ]
        
        #Widget multi-select interaktif bawaan Streamlit
        gejala_dipilih = st.multiselect("Pilih satu atau beberapa gejala lambung:", daftar_opsi_gejala)
        
        #Poin/Syarat B: Operator (Desain layout tombol proses) 
        st.write("")
        if st.button("🚀 Proses Analisis Lambung", use_container_width=True):
            if len(gejala_dipilih) == 0:
                st.warning("⚠️ Silakan pilih minimal satu gejala lambung terlebih dahulu sebelum menekan tombol proses.")
            else:
                st.write("---")
                st.subheader("🩺 Hasil Analisis Medis Sementara")

                #Memanggil Fungsi Logika Medis
                hasil_medis = diagnosa_penyakit(gejala_dipilih)

                #Menampilkan 1 kotak rekomendasi utama
                st.success(f"Rekomendasi Sistem: {hasil_medis}")

                #Disclaimer 
                st.caption("Disclaimer: Aplikasi ini hanyalah sistem pakar deteksi awal gangguan lambung. Jika nyeri ulu hati sangat hebat atau disertai muntah darah/BAB hitam, segera hubungi dokter atau IGD terdekat.")