# Lab-6.py

### Nama : Arifin Syahrul Azhadi Harahap

### NIM : 352310965

### Kelas : IE.23.C.13

### Mata Kuliah : Program Komputer + Praktek

### Dosen : Agung Nugroho, S.Kom., M.Kom.
_________________________________________________________________________________________________________________________________________________________________________________________

## Tugas Praktikum (Buat program sederhana dengan mengaplikasikan penggunaan fungsi)

## A. Algoritma Program

1, Mulai

Tampilkan pesan pembuka program.

2, Tampilkan Menu

Tampilkan opsi berikut:
* 1: Tambah Data Mahasiswa
* 2: Tampilkan Data Mahasiswa
* 3: Hapus Data Mahasiswa
* 4: Ubah Data Mahasiswa
* 5: Keluar
  
3, Input Pilihan

Pengguna memasukkan pilihan menu.

4, Percabangan Berdasarkan Pilihan

Jika pilihan = 1:

a. Input nama mahasiswa.

b. Input nilai mahasiswa.

c. Tambahkan data (nama dan nilai) ke dalam daftar.

d. Tampilkan pesan "Data berhasil ditambahkan."

e. Kembali ke langkah 2.


Jika pilihan = 2:

a. Periksa apakah daftar mahasiswa kosong.
* Jika kosong, tampilkan pesan "Tidak ada data mahasiswa."
* Jika tidak, tampilkan semua data mahasiswa. Kembali ke langkah 2.

Jika pilihan = 3:

a. Input nama mahasiswa yang akan dihapus.

b. Cari data berdasarkan nama.

* Jika ditemukan, hapus data dari daftar, dan tampilkan pesan "Data berhasil dihapus."
* Jika tidak ditemukan, tampilkan pesan "Nama tidak ditemukan."

c. Kembali ke langkah 2.

Jika pilihan = 4:

a. Input nama mahasiswa yang akan diubah.

b. Cari data berdasarkan nama.
* Jika ditemukan, input nilai baru dan perbarui data, lalu tampilkan pesan "Data berhasil diubah."
* Jika tidak ditemukan, tampilkan pesan "Nama tidak ditemukan."

c. Kembali ke langkah 2.

Jika pilihan = 5:

a. Tampilkan pesan "Program selesai."

b. Akhiri program.


Jika pilihan salah:

a. Tampilkan pesan "Pilihan tidak valid."

b. Kembali ke langkah 2.

5, Selesai

## B. Gambar Flowchart Program

![Flow Chart Lab 6 py drawio](https://github.com/user-attachments/assets/c1551849-3e1a-4c5a-8ddd-c5f0643f4e61)

## C. Menampilkan Program dan penjelasan Yang telah dibuat menggunakan program penggunaan "Fungsi"

![Gambar Program 1](https://github.com/user-attachments/assets/c8e0311b-d4aa-4d77-8268-df17963329c2)

![Gambar Program 2](https://github.com/user-attachments/assets/d0a67a95-2a74-467c-a0f5-dc2b5f2825b6)

Berikut penjelasan programnya;

1, Inisialisasi Program

Langkah:
* Buat daftar kosong untuk menyimpan data mahasiswa.

![image](https://github.com/user-attachments/assets/6f0bcb29-e926-4e93-a1a0-cb4d8e2e5e0f)


Penjelasan:

* Daftar ini akan menjadi tempat penyimpanan data mahasiswa, di mana setiap elemen berupa dictionary ({"nama": ..., "nilai": ...}).

3, Definisikan Fungsi Tambah Data

Langkah:
* Buat fungsi tambah() untuk menambah data mahasiswa.

![image](https://github.com/user-attachments/assets/c7732e2b-4249-460d-ab8c-68b47d254e39)

Penjelasan:
* Fungsi ini meminta pengguna untuk memasukkan nama dan nilai mahasiswa.
* Data mahasiswa akan disimpan dalam daftar data_mahasiswa.
* Fungsi menggunakan append() untuk menambahkan dictionary ke daftar.

3, Definisikan Fungsi Tampilkan Data

Langkah:
* Buat fungsi tampilkan() untuk menampilkan semua data mahasiswa.

![image](https://github.com/user-attachments/assets/97642f84-3c38-48b7-9785-8340715150af)

Penjelasan:
* Fungsi ini memeriksa apakah daftar data_mahasiswa kosong.
* Jika tidak kosong, fungsi mencetak semua data mahasiswa dengan penomoran menggunakan enumerate().

4, Definisikan Fungsi Hapus Data

Langkah:
* Buat fungsi hapus(nama) untuk menghapus data berdasarkan nama.

![image](https://github.com/user-attachments/assets/a27eeb07-0f80-4d62-ac28-7beb28939651)

Penjelasan:
* Fungsi ini mencari data mahasiswa berdasarkan nama.
* Jika nama ditemukan, data dihapus menggunakan remove(). Jika tidak ditemukan, pesan kesalahan ditampilkan.

5, Definisikan Fungsi Ubah Data

Langkah:
* Buat fungsi ubah(nama) untuk mengubah nilai berdasarkan nama.
python

![image](https://github.com/user-attachments/assets/2f08ffe0-7e1e-4e16-8daa-b1fb7ca5203a)

Penjelasan:
* Fungsi ini mencari data mahasiswa berdasarkan nama.
* Jika ditemukan, meminta input nilai baru dan memperbarui data.
* Jika tidak ditemukan, menampilkan pesan kesalahan.

6, Buat Menu Utama

Langkah:
* Buat loop utama untuk menampilkan menu dan memanggil fungsi yang sesuai.

![image](https://github.com/user-attachments/assets/c6f6aa93-93e0-48c7-91f1-04839a77c06f)

Penjelasan:
* Menu menggunakan loop while True agar terus berjalan sampai pengguna memilih keluar (pilihan = 5).
* Pilihan menu menentukan fungsi mana yang akan dijalankan.
* Jika input tidak valid, program akan memberikan pesan kesalahan dan kembali ke menu.

7, Uji Program

Langkah:
* Jalankan program dan uji setiap fungsi:
* Tambah data: Pastikan data tersimpan dengan benar.
* Tampilkan data: Periksa apakah data ditampilkan sesuai format.
* Hapus data: Coba hapus data yang ada dan yang tidak ada.
* Ubah data: Ubah nilai data yang ada dan periksa pembaruan.
* Keluar program: Pastikan program keluar dengan benar.

Penjelasan:
* Uji coba memastikan semua fungsi berjalan sesuai yang diharapkan dan menangani kesalahan input pengguna.

## D. Hasil Program yang telah dijalankan dengan mengklik "Run"

![Hasil Program 1](https://github.com/user-attachments/assets/56d82a3f-f891-4465-8e26-c05467374ebf)

![Hasil Program 2](https://github.com/user-attachments/assets/287e8555-8921-46b1-9e86-6a8c4c41e481)


### Selesai
