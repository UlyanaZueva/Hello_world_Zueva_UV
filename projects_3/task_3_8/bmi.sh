#!/bin/bash

read -p "Введите рост (в метрах): "  HEIGHT
read -p "Введите массу (в кг): " WEIGHT
BMI=$(echo "scale=0; $WEIGHT / ($HEIGHT * $HEIGHT)" | bc)
echo "Ваш индекс массы тела: $BMI"

