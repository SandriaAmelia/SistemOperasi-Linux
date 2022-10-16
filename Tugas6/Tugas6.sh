#!/bin/bash

printf "Input total semester selanjutnya IPS : "
read n

declare -a arrayIPSMahasiswa

i=0
let jumlah=$n-1

while [ $i -le $jumlah ];
do
   let nilai=$i+1
   printf " " $nilai;
   read nilaisem;
   arrayIPSMahasiswa[$i]=$nilaisem;
   let total+=$nilaisem;
   let i=$i+1;
done

let IPK=$total/$n
echo "IPK mhs = " $total / $n
echo "IPK mhs = " $IPK
