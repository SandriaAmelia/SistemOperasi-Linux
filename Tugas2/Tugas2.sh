printf "Berapa pengeluaran anda bulan September?"

read pengeluaranSept

if [ $pengeluaranSept > 500000 ]
then
 echo "Pengeluaran anda bulan September lebih dari budget"
elif [ $pengeluaranSept < 500000 ]
then
 echo "Pengeluaran anda bulan September kurang dari budget"
else
 echo "Selamat!! Pengeluaran anda bulan September sesuai budget"
fi
