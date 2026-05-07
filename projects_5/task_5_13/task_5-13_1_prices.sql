--Увеличьте цену на 10% для всех товаров, у которых текущая цена меньше 1000

--Проверяем данные перед обновлением:
select *
from prices 
where price < 1000;


--Обновляем данные с помощью UPDATE:
update prices 
set price = price * 1.1
where price < 1000;

--Проверяем данные после обновления:
select *
from prices;