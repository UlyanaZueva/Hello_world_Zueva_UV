--Выведите записи из таблицы prices, где цена находится в диапазоне от 1000 до 50000 включительно
select *  
from prices 
where price between 1000 and 50000;


--Выведите цены товаров (prices), у которых:
--price находится в диапазоне от 500 до 70000;
--и product_id меньше или равен 5;
select price 
from prices 
where (price between 550 and 70000) and (product_id between 1 and 5);


--Выведите цены товаров, которые:
--меньше 100 или;
--находятся в диапазоне от 60000 до 70000
select price
from prices 
where (price between 1 and 100) or (price between 60000 and 70000);


