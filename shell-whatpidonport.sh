#!/bin/env bash
if [ "$1" != "" ]; then
    echo "portnumtocheckis  is  missing"
    exit
fi
netstat -ltnp | grep -w ':$1' 
#lsof -i :80
#fuser 80/tcp
#ps -p 2053 -o comm=
