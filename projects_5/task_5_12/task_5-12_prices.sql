-- Выведите количество (COUNT) записей в таблице prices для каждого товара (product_id)
select product_id, count (*)
from prices
group by product_id
order by product_id;


-- Выведите среднюю цену товаров (AVG(price)) для каждого product_id из таблицы prices
select product_id, AVG(price)
from prices 
group by product_id
order by product_id;


--Выведите минимальную (MIN) цену для каждого товара (product_id) из таблицы prices
select product_id, MIN(price)
from prices 
group by product_id
order by product_id;


--Выведите максимальную (MAX) цену для каждого товара (product_id) из таблицы prices
select product_id, MAX(price)
from prices 
group by product_id
order by product_id;
