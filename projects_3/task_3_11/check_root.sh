#!/bin/bash

check_root() {
    if [ $EUID -ne 0 ]; then
        echo "Ошибка: Этот скрипт должен запускаться от root"
        echo "Попробуйте: sudo $0"
        exit 1
    fi
}

check_root

echo "Скрипт успешно запущен от root"
echo "Выполняются административные задачи..."

