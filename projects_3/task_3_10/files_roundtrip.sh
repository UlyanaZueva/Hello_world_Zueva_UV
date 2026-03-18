#!/bin/bash

echo "Создание файлов:"
for i in {1..10}; do
    touch "test$i.txt"
    echo "test$i.txt создан"
done

echo -e "\nУдаление файлов в обратном порядке:"
i=10
while [ $i -ge 1 ]; do
    rm "test$i.txt"
    echo "test$i.txt удален"
    i=$((i - 1))
done

