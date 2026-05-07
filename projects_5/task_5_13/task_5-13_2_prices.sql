--Обновите цены товаров для записей, где product_id ≤ 5 и цена меньше 10000, увеличить цену на 5%

--Проверяем данные перед обновлением:
select *
from prices 
where product_id <= 5 and price < 10000;


--Обновляем данные с помощью UPDATE:
update prices 
set price = price * 1.05
where product_id <= 5 and price < 10000;

--Проверяем данные после обновления:
select *
from prices;