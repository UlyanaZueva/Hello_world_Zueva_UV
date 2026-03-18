#!/bin/bash

if [ ! -f data.csv ]; then
    echo "Ошибка: файл data.csv не найден!"
    exit 1
fi

echo "Названия товаров:"
awk -F "," '{print $2}' data.csv

echo -e "\nТовары дороже 20:"
awk -F "," '$3 > 20' data.csv

echo -e "\nОбщая стоимость:"
awk -F "," '{sum += $3} END {print sum}' data.csv
