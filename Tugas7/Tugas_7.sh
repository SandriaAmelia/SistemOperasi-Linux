#!/bin/bash

# Mendeklarasikan fungsi
panjang() {
    echo "Masukkan Panjang : "
    read panjang
}
lebar() {
    echo "Masukkan Lebar : "
    read lebar
    let luaspersegi=$panjang*$lebar
    echo "Luas Persegi :
$luaspersegi"
}

# Memanggil Fungsi
panjang
lebar
