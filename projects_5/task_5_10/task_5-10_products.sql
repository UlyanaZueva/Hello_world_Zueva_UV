--Вывести все товары из таблицы products
select *
from products;

--Выведите только название (name) и категорию (category) всех товаров из таблицы products
select name, category
from products;

--Выведите список всех уникальных категорий товаров из таблицы products
select distinct category
from products;

--Выведите все товары из таблицы products, отсортированные по названию в алфавитном порядке
select name 
from products
order by name asc;

--Выведите все товары из таблицы products, отсортированные по названию в обратном алфавитном порядке
select name 
from products
order by name desc;

--Выведите первые 10 товаров из таблицы products
select name 
from products
limit 10;

--Выведите 10 товаров из таблицы products, начиная с 11-й записи
select name 
from products
limit 10 offset 10;

--Выведите 5 случайных товаров из таблицы products. (Для решения используйте ORDER BY RANDOM() и LIMIT)
select name 
from products
ORDER BY RANDOM()
limit 5;

--Выведите все категории товаров из таблицы products (без использования DISTINCT), отсортированные по алфавиту (Используйте ORDER BY category ASC)
select category
from products
ORDER BY category asc;

--Выведите все товары из таблицы products, отсортированные сначала по категории, затем по названию
select *
from products  
order by category, name asc; 

