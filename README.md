# Studi_Kasus_3_Shaina-Naila-Raihana
Nama : Shaina Naila Raihana
NIM : 090

PENJELASAN PROGRAM

<img width="524" height="149" alt="satu" src="https://github.com/user-attachments/assets/d51e4f29-9334-4528-950b-f87f93f78c9c" />

- batas_nilai = (65, 100)
digunakan untuk menentukan batas nilai, yaitu 65 sampai 100.

- nilai_masuk = []
digunakan untuk menyimpan semua nilai yang dimasukkan.

- lulus = []
digunakan untuk menyimpan nilai yang dinyatakan lulus.

- remedial = []
digunakan untuk menyimpan nilai yang masuk kategori remedial.

<img width="965" height="374" alt="kedua beneran" src="https://github.com/user-attachments/assets/a7b74299-cf69-41ee-b370-be968739efd6" />

- for i in range(100):
digunakan untuk melakukan perulangan input nilai maksimal 100 kali.

- nilai = input("masukkan nilai: ")
digunakan untuk meminta pengguna memasukkan nilai.

- if nilai == "selesai":
digunakan untuk mengecek apakah pengguna mengetik "selesai".

- break
digunakan untuk menghentikan perulangan ketika pengguna mengetik "selesai".

- nilai = int(nilai)
digunakan untuk mengubah input nilai menjadi bilangan bulat.

- nilai_masuk.append(nilai)
digunakan untuk memasukkan nilai ke dalam list nilai_masuk.

- if nilai >= batas_nilai[0]:
digunakan untuk mengecek apakah nilai lebih besar atau sama dengan 65.

- lulus.append(nilai)
digunakan untuk memasukkan nilai yang memenuhi batas kelulusan ke list lulus.

- else:
digunakan ketika nilai tidak memenuhi kondisi kelulusan.

- remedial.append(nilai)
digunakan untuk memasukkan nilai yang kurang dari 65 ke list remedial.

<img width="652" height="91" alt="ketiga" src="https://github.com/user-attachments/assets/99cc285c-8d39-4b2f-89ff-8d6092153143" />

- print("nilai masuk:", nilai_masuk)
digunakan untuk menampilkan seluruh nilai yang telah dimasukkan.

- print("nilai lulus:", lulus)
digunakan untuk menampilkan nilai yang lulus.

- print("nilai remedial:", remedial)
digunakan untuk menampilkan nilai yang masuk remedial.

<img width="860" height="141" alt="keempat" src="https://github.com/user-attachments/assets/d273b7f7-70b5-408c-aa38-0d7180616f08" />

- hapus = int(input("masukkan nilai yang ingin dihapus: "))
digunakan untuk meminta user memilih nilai yang ingin dihapus.

- nilai_masuk.remove(hapus)
digunakan untuk menghapus nilai yang telah dipilih dari list.

- print("nilai akhir:", nilai_masuk)
digunakan untuk menampilkan daftar nilai setelah dilakukan penghapusan.

HASIL PROGRAM
<img width="1920" height="1080" alt="Screenshot (429)" src="https://github.com/user-attachments/assets/a1253d47-8cb5-4544-8adc-12827b2451e5" />
<img width="1920" height="1080" alt="Screenshot (430)" src="https://github.com/user-attachments/assets/a2e674e2-e6b8-4c52-b413-1281f0b89956" />

berdasarkan hasil yang ditampilkan, user memasukkan lima nilai, yaitu 70, 50, 80, 60, dan 90. setelah mengetik "selesai", program mengelompokkan nilai menjadi nilai lulus [70, 80, 90] dan nilai remedial [50, 60]. kemudian user memilih nilai 50 untuk dihapus. setelah penghapusan, hasil akhirnya menjadi [70, 80, 60, 90].
