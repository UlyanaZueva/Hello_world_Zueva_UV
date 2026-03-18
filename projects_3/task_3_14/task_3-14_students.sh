#!/bin/bash

echo "Имена студентов:"
awk '{print $1}' students.txt

echo -e "\nОценки студентов:"
awk '{print $2}' students.txt

echo -e "\nНомер строки и имя:"
awk '{print NR, $1}' students.txt
