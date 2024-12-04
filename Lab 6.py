# Daftar untuk menyimpan data mahasiswa
data_mahasiswa = []

# Fungsi untuk menambah data mahasiswa
def tambah():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai tugas: "))
    nilai = float(input("Masukkan nilai UTS: "))
    nilai = float(input("Masukkan nilai UAS: "))
    data_mahasiswa.append({"nama": nama, "nilai": nilai})
    print(f"Data mahasiswa {nama} berhasil ditambahkan.\n")

# Fungsi untuk menampilkan data mahasiswa
def tampilkan():
    if not data_mahasiswa:
        print("Tidak ada data mahasiswa.\n")
    else:
        print("Daftar Nilai Mahasiswa:")
        for i, mhs in enumerate(data_mahasiswa, start=1):
            print(f"{i}. Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")
        print()

# Fungsi untuk menghapus data mahasiswa berdasarkan nama
def hapus(nama):
    global data_mahasiswa
    for mhs in data_mahasiswa:
        if mhs['nama'] == nama:
            data_mahasiswa.remove(mhs)
            print(f"Data mahasiswa {nama} berhasil dihapus.\n")
            return
    print(f"Mahasiswa dengan nama {nama} tidak ditemukan.\n")

# Fungsi untuk mengubah data mahasiswa berdasarkan nama
def ubah(nama):
    for mhs in data_mahasiswa:
        if mhs['nama'] == nama:
            nilai_baru = float(input("Masukkan nilai baru: "))
            mhs['nilai'] = nilai_baru
            print(f"Data mahasiswa {nama} berhasil diubah.\n")
            return
    print(f"Mahasiswa dengan nama {nama} tidak ditemukan.\n")

# Menu utama
while True:
    print("=== Menu ===")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Hapus Data Mahasiswa")
    print("4. Ubah Data Mahasiswa")
    print("5. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama_hapus = input("Masukkan nama mahasiswa yang akan dihapus: ")
        hapus(nama_hapus)
    elif pilihan == "4":
        nama_ubah = input("Masukkan nama mahasiswa yang akan diubah: ")
        ubah(nama_ubah)
    elif pilihan == "5":
        print("Program selesai. Terima kasih.")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.\n")
