#!/bin/env bash

if [ "$1" != "" ]; then
 	[[ "$1" =~ ^[[:alnum:]]+$ ]] && [[ ! "$1" =~ ^[[:digit:]]+$ ]] && echo ok
else
    echo "processnametomonitor is  missing"
    exit
fi

for x in {1..100}; do
sleep 2;
#DATE=`date`
#DATE2=`echo $DATE | sed 's/,/|/g'`
ps axo ruser,%cpu,%mem,pid,command|sort -nr |grep $1
ps axo ruser,%cpu,%mem,pid,command|sort -nr |grep $1 |awk -v DATE="$(date +"%Y-%m-%d %r")" '{s+=$2;m+=$3} END {printf "DateTime=>%s,CPU=>%.0f,MEM=>%.0f\n",DATE,s,m}'
done
