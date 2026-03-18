#!/bin/bash


for i in {1..20}; do
    if [ $((i % 2)) -eq 0 ]; then
        continue
    fi
   
    if [ $i -eq 15 ]; then
        # Если встретили 15 - прерываем цикл
        break
    fi
    
    echo $i
done
 
