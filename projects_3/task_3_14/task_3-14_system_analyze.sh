#!/bin/bash

df -h | awk 'NR>1 {
    filesystem=$1
    usage=$5
    gsub(/%/, "", usage)
    printf "Файловая система: %s, Заполнение: %s%%\n", filesystem, $5
    if (usage > 90) {
        printf "  ВНИМАНИЕ: заполнение превышает 90%%!\n"
    }
}'
