import streamlit as st
import time

# 1. Membuat judul aplikasi
st.title("📢 Digital Marketing: Sistem Blast Notifikasi")
st.write("Gunakan `for loop` untuk memproses daftar data yang sudah pasti jumlahnya.")

# 2. Membuat daftar data (Koleksi data yang akan di-loop)
daftar_pelanggan = ["Budi", "Siti", "Andi", "Rani", "Dewi", "kusuma", "Dodi"]

# Menampilkan daftar pelanggan di UI
st.write(f"👥 **Daftar Target Konsumen ({len(daftar_pelanggan)} orang):**")
st.info(", ".join(daftar_pelanggan))

# Kolom input untuk isi pesan
pesan_promo = st.text_input("Tulis Pesan Promo Anda:", "Halo! Dapatkan diskon 50% khusus hari ini!")

# 3. Tombol Eksekusi
if st.button("Mulai Kirim Massal 🚀", type="primary"):
    
    # Menyiapkan komponen visual dinamis
    tampilan_status = st.empty()
    tampilan_progress = st.progress(0.0)
    
    total_target = len(daftar_pelanggan)
    
    st.markdown("---")
    st.subheader("📊 Log Pengiriman Real-Time:")
    
    # --- DI SINI IMPLEMENTASI FOR LOOP DI DUNIA NYATA ---
    # Loop akan mengambil satu per satu 'nama' dari 'daftar_pelanggan'
    for indeks, nama in enumerate(daftar_pelanggan):
        
        # Tampilkan status siapa yang sedang diproses saat ini
        tampilan_status.warning(f"⏳ Sedang mengirim pesan ke: **{nama}** (Antrean ke-{indeks + 1})...")
        
        # Simulasi jeda waktu pengiriman (agar tidak diblokir/dianggap spam oleh server)
        time.sleep(2)
        
        # Cetak laporan sukses ke layar untuk setiap orang
        st.write(f"✅ [SUKSES] Pesan terkirim ke **{nama}** -> *'{pesan_promo}'*")
        
        # Hitung dan update progress bar (Nilai harus di antara 0.0 sampai 1.0)
        progress_sekarang = (indeks + 1) / total_target
        tampilan_progress.progress(progress_sekarang)

    # --- KODE DI LUAR LOOP (EKSEKUSI SETELAH SEMUA ELEMEN SELESAI) ---
    tampilan_status.success(f"🎉 Selesai! Semua ({total_target}) pesan telah berhasil dikirim otomatis.")