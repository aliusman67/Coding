print("Operasi String")

#fusion string = penggabungan 2 string atau lebih

str1 = "Hello"
str2 = "World"

#cara 1
print("Hasil", str1 + str2)
#cara 2 
print("Hasil", str1, str2)

#looping string
kata = "Hello "
kali = kata * 5
print(kali)

#mendapatkan informasi panjang dari sebuah data menggunakan len()
kalimat = "Hello, perkenalakna nama saya John Doe"
panjang = len(kalimat)
print(panjang)

#mengakses karakter dalam string
Kata = "Hello, World"
substring = kata[0] #mengakses karakter didalam sebuah string berdasakan index
print(substring)

#slicing karakter dalam sebuah string
kata1 = "Halo, Dunia"
substring1 = kata1[0:5] #slicing karakter dari index 0 ke 5
substring2 = kata1[:3] #memotong dari awal hingga index tertentu
substring3 = kata1[5:] #Memotong dari indeks tertentu hingga akhir
print(substring1)
print(substring2)
print(substring3)

#mengecek keberadaan string
buah = input("Masukan Nama Buah: ")
data = "Apel, Manggis, Jambu, Nanas"

if buah in data:
    print("data ditemukan")
elif buah not in data:
    print("Tidak ditemukan data")

#mencari kata dalam sebuah kalimat function find()
kalimat = """Halo nama saya Budi, Budi bersekolah di SMK Palangkaraya
            Sekarang Budi menginjak kelas 12 SMK Palangakaraya 15"""
cari = kalimat.find("Budi")

print(cari)
