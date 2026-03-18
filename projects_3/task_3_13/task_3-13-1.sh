#!/bin/bash
sed -i '' 's|/var/lib/mysql/data|/mnt/ssd/mysql|g' settings.php
echo "Путь к базе данных в settings.php успешно заменен!"
