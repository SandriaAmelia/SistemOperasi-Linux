total = []

print("=============== KASIR SUN ===============")
Pembeli = input("Nama Pembeli : ")
print(" ")
print("-"*41)
print("Daftar diskon\n1) Belanja di atas Rp100.000 disc 1%\n2) Belanja di atas Rp200.000 disc 4%\n3) Belanja di atas Rp350.000 disc 7%")
print("-"*41)

def daftar_barang():
    print(" ")
    print("-"*41)
    print("| KODE |      NAMA BARANG      | HARGA |")
    print("-"*41)
    print("|  1  | Keju Wincheez 250gr     | 13000 |")
    print("|  2  | V-SOY Original 1L       | 33000 |")
    print("|  3  | Tepung terigu 1kg       | 16000 |")
    print("|  4  | Whipped Cream 100gr     | 14500 |")
    print("|  5  | Blueband 200gr          | 13000 |")
    print("|  6  | Nestle SKM  495gr       | 15500 |")
    print("|  7  | Cocoa powder 100gr      | 17500 |")
    print("|  8  | Meses warna warni 250gr | 16000 |")
    print("|  9  | Toffieco Pasta 50gr     | 23000 |")
    print("-"*41)
    kode = int(input("Masukkan kode barang  : "))
    if kode == 1:
        jumlah1 = int(input("Jumlah barang : "))
        total1 = 13000 * jumlah1
        total.append(total1)
        tanya()
    elif kode == 2:
        jumlah2 = int(input("Jumlah barang : "))
        total2 = 33000 * jumlah2
        total.append(total2)
        tanya()
    elif kode == 3:
        jumlah3 = int(input("Jumlah barang : "))
        total3 = 16000 * jumlah3
        total.append(total3)
        tanya()
    elif kode == 4:
        jumlah4 = int(input("Jumlah barang : "))
        total4 = 14500 * jumlah4
        total.append(total4)
        tanya()
    elif kode == 5:
        jumlah5 = int(input("jumlah barang : "))
        total5 = 13000 * jumlah5
        total.append(total5)
        tanya()
    elif kode == 6:
        jumlah6 = int(input("Masukkan jumlah barang : "))
        total6 = 15500 * jumlah6
        total.append(total6)
        tanya()
    elif kode == 7:
        jumlah7 = int(input("Masukkan jumlah barang : "))
        total7 = 17500 * jumlah7
        total.append(total7)
        tanya()
    elif kode == 8:
        jumlah8 = int(input("Masukkan jumlah barang : "))
        total8 = 16000 * jumlah8
        total.append(total8)
        tanya()
    elif kode == 9:
        jumlah9 = int(input("Masukkan jumlah barang : "))
        total9 = 23000 * jumlah9
        total.append(total9)
        tanya()
    else:
        print("Pilihan tidak ada di daftar barang\nSilahkan pilih kembali !!!")
        daftar_barang()
    return

def tanya():
    print(" ")
    print("-"*41)
    tanya = input("Ingin tambah barang?\nTekan [YES/NO] : ")
    print("-"*41)
    if tanya == "YES":
        daftar_barang()
    elif tanya == "NO":
        akhir()
    else:
        print("Pilihan yang anda masukan salah\nSilahkan pilih kembali !!!")

def akhir():
    for harga in total:
        diskon = 0
        a = sum(total)
        if a > 350000:
            diskon = a * 7/100
        elif a > 200000:
            diskon = a * 4/100
        elif a > 100000:
            diskon = a * 1/100
        else:
            diskon = 0
        print("\n======= S T R U K  B E L A N J A ========")
        print("Nama\t\t:",Pembeli)
        print("SubTotal\t: Rp", sum(total))
        print("Diskon\t\t: Rp", diskon)
        totalakhir = a - diskon
        print("Tagihan\t\t: Rp", totalakhir)
        bayar = int(input("Dibayar\t\t: Rp "))
        kembalian = bayar - totalakhir
        print("Kembalian\t: Rp", kembalian)
        print("="*41)
        print("               Terima Kasih              ")
        print("="*41)
        break

daftar_barang()
