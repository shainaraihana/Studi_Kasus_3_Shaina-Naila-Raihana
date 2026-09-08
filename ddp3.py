batas_nilai = (65, 100)

nilai_masuk = []
lulus = []
remedial = []

for i in range(100):
    nilai = input("Masukkan nilai: ")

    if nilai == "selesai":
        break

    nilai = int(nilai)
    nilai_masuk.append(nilai)

    if nilai >= batas_nilai[0]:
        lulus.append(nilai)
    else:
        remedial.append(nilai)

print("nilai masuk:", nilai_masuk)
print("nilai lulus:", lulus)
print("nilai remedial:", remedial)

hapus = int(input("masukkan nilai yang ingin dihapus: "))

nilai_masuk.remove(hapus)

print("nilai akhir:", nilai_masuk)