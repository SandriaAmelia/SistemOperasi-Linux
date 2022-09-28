echo "Pemrograman kelipatan ganjil menurun."
echo "Masukkan acuan bilangan : "
read x

while [ $((x%2)) -eq 1 ]
do
  echo "x merupakan bilangan ganjil."
  for ((x=$x; x>-1; x=x-2))
  do
    echo $x
  done
done

echo "Pemrograman kelipatan ganjil naik."
echo "Masukkan acuan bilangan : "
read y
echo "y merupakan bilangan ganjil."
while [ $((y%2)) -eq 1 ]
do
  until [ ! $y -lt 100 ]
  do
    echo $y
    y=$((y+2))
  done
done

echo "Selesai."
