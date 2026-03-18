#!/bin/bash
sed -i '' 's/ /\t/g' sequences.txt
echo "Пробелы заменены на табуляцию в файле sequences.txt"
