import streamlit as st
import time

# 1. Membuat judul aplikasi
st.title("🚰 IoT Simulator: Sistem Pompa Air Otomatis")
st.write("Gunakan `while loop` untuk mematikan pompa ketika tangki penuh.")

# 2. Membuat input komponen fisik (simulasi)
kapasitas_maksimal = st.number_input("Kapasitas Maksimal Tangki (Liter):", value=100, step=10)
kecepatan_pompa = st.slider("Kecepatan Aliran Pompa (Liter / Detik):", min_value=1, max_value=25, value=10)

# 3. Tombol Saklar Pompa
if st.button("Nyalakan Pompa Air 🚀", type="primary"):
    
    # Inisialisasi kondisi awal air di dalam tangki
    air_sekarang = 0
    
    # Menyiapkan tempat visualisasi di Streamlit
    tampilan_status = st.empty()
    tampilan_progress = st.progress(0)
    
    # --- DI SINI IMPLEMENTASI WHILE LOOP DI DUNIA NYATA ---
    while air_sekarang < kapasitas_maksimal:
        # Air bertambah sesuai kecepatan pompa
        air_sekarang = air_sekarang +  kecepatan_pompa
        
        # Antisipasi agar air tidak melebihi kapasitas di visualisasi
        if air_sekarang > kapasitas_maksimal:
            air_sekarang = kapasitas_maksimal
            
        # Update tampilan dashboard secara real-time
        tampilan_status.metric(
            label="Volume Air di Dalam Tangki", 
            value=f"{air_sekarang} Liter", 
            delta=f"+{kecepatan_pompa} L/detik"
        )
        
        # Update progress bar (harus bernilai antara 0.0 sampai 1.0)
        tampilan_progress.progress(air_sekarang / kapasitas_maksimal)
        
        # Memberikan jeda waktu simulasi seolah-olah air sedang mengalir
        time.sleep(0.5)
        
    # --- KODE DI LUAR LOOP (EKSEKUSI SETELAH WHILE BERNILAI FALSE) ---
    st.success("🎉 SENSOR MENDETEKSI TANGKI PENUH! Pompa dimatikan otomatis.")