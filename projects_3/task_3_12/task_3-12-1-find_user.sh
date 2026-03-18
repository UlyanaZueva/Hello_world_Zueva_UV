#!/bin/bash

echo "=== Поиск пользователя $USER в файле /etc/passwd ==="
echo ""

grep "^$USER" /etc/passwd

if [ $? -eq 0 ]; then
    echo ""
    echo "Пользователь $USER найден!"
else
    echo ""
    echo "Пользователь $USER не найден в системе"
fi
