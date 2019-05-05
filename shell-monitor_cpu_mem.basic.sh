#!/bin/env bash

if [ "$1" != "" ]; then
 	[[ "$1" =~ ^[[:alnum:]]+$ ]] && [[ ! "$1" =~ ^[[:digit:]]+$ ]] && echo ok
else
    echo "processnametomonitor is  missing"
    exit
fi

for x in {1..100}; do
sleep 2;
date ;
ps axo ruser,%cpu,%mem,pid,command|sort -nr |grep $1;
ps axo ruser,%cpu,%mem,pid,command|sort -nr |grep $1 |awk '{s+=$2;m+=$3} END {printf "CPU=>%.0f,MEM=>%.0f\n",s,m}'
#ps axo ruser,%cpu,%mem,pid,command|sort -nr |grep stress;
#ps axo ruser,%cpu,%mem,pid,command|sort -nr |grep stress |awk '{s+=$2;m+=$3} END {printf "CPU=>%.0f,MEM=>%.0f\n",s,m}'
done
