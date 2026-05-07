-- Выведите количество товаров в таблице products, сгруппировав результат по категориям
select category, count(*)
from products 
group by category;

--Выведите количество товаров в каждой категории из таблицы products, отсортировав результат по убыванию количества
select category, count(*)
from products 
group by category
order by count(*) desc;