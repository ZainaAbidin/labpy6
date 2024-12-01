# Daftar untuk menyimpan data mahasiswa
mahasiswa = []

def tambah(nama, nilai):
    """Menambah data mahasiswa ke dalam daftar."""
    mahasiswa.append({'nama': nama, 'nilai': nilai})
    print(f"Data {nama} berhasil ditambahkan.")

def tampilkan():
    """Menampilkan semua data mahasiswa."""
    if not mahasiswa:
        print("Tidak ada data mahasiswa.")
        return
    
    print("Daftar Nilai Mahasiswa:")
    for idx, mhs in enumerate(mahasiswa, start=1):
        print(f"{idx}. Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")

def hapus(nama):
    """Menghapus data mahasiswa berdasarkan nama."""
    global mahasiswa
    mahasiswa = [mhs for mhs in mahasiswa if mhs['nama'] != nama]
    print(f"Data {nama} berhasil dihapus.")

def ubah(nama, nilai_baru):
    """Mengubah data mahasiswa berdasarkan nama."""
    for mhs in mahasiswa:
        if mhs['nama'] == nama:
            mhs['nilai'] = nilai_baru
            print(f"Data {nama} berhasil diubah menjadi nilai {nilai_baru}.")
            return
    print(f"Data {nama} tidak ditemukan.")

# Menu interaktif untuk pengguna
def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Hapus Data Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama mahasiswa: ")
            nilai = float(input("Masukkan nilai mahasiswa: "))
            tambah(nama, nilai)
        elif pilihan == '2':
            tampilkan()
        elif pilihan == '3':
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            hapus(nama)
        elif pilihan == '4':
            nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            nilai_baru = float(input("Masukkan nilai baru mahasiswa: "))
            ubah(nama, nilai_baru)
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    main()
