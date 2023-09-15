print("""
 ____  _                 _        _  __     _ _          _       _             
/ ___|(_)_ __ ___  _ __ | | ___  | |/ /__ _| | | ___   _| | __ _| |_ ___  _ __ 
\___ \| | '_ ` _ \| '_ \| |/ _ \ | ' // _` | | |/ / | | | |/ _` | __/ _ \| '__|
 ___) | | | | | | | |_) | |  __/ | . \ (_| | |   <| |_| | | (_| | || (_) | |   
|____/|_|_| |_| |_| .__/|_|\___| |_|\_\__,_|_|_|\_\\__,_|_|\__,_|\__\___/|_|   
                  |_|                                                          
""")
print("""
    1. Pejumlahan
    2. Pengurangan
    3. Perkalian
    4. Pembagian
    5. Luas Persegi Panjang
""")

#function penjumlahan
def tambah(input_1, input_2):
    tambah = input_1 + input_2
    return tambah

#function pengurangan
def kurang(input_1, input_2):
    kurang = input_1 - input_2
    return kurang

#function perkalian
def kali(input_1, input_2):
    kali = input_1 * input_2
    return kali

#function pembagian
def bagi(nilai_1, nilai_2):
     bagi = nilai_1 / nilai_2
     return bagi
def luas(nilai_1, nilai_2):
    luas = nilai_1 * nilai_2
    return luas
pilih = int(input("Pilih Menu: "))

nilai_1 = int(input("Masukan Nilai Pertama: "))
nilai_2 = int(input("Masukan Nilai Kedua: "))

if pilih == 1:
    print(f"Hasil dari penjumlahan {nilai_1} + {nilai_2} adalah", tambah(nilai_1, nilai_2))
elif pilih == 2:
    print(f"Hasil dari pengurangan {nilai_1} - {nilai_2} adalah", kurang(nilai_1, nilai_2))
elif pilih == 3:
    print(f"Hasil dari perkalian {nilai_1} x {nilai_2} adalah", kali(nilai_1, nilai_2))
elif pilih == 4:
    print(f"Hasil dari pembagian {nilai_1} / {nilai_2} adalah", bagi(nilai_1, nilai_2))
elif pilih == 5:
    print(f"Luas dari persegi panjangn yang panjangnya {nilai_1} dan lebar {nilai_2} adalah", luas(nilai_1, nilai_2), "cm")