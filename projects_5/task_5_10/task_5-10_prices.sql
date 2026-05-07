-- Выведите 5 самых дорогих записей из таблицы prices
select * 
from prices
order by price desc 
limit 5;

-- Выведите 10 последних добавленных записей из таблицы prices, отсортированных по полю created_at
select * 
from prices
order by created_at desc 
limit 10;

--Выведите 10 самых дешёвых цен из таблицы prices
select price  
from prices
order by price asc 
limit 10;

--Выведите записи из таблицы prices: пропустите первые 20 самых дорогих значений
select *  
from prices
order by price desc 
offset 20;
