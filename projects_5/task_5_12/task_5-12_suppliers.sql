--Выведите количество поставщиков для каждого товара из таблицы suppliers, сгруппировав данные по product_id
select product_id, count (*)
from suppliers
group by product_id
ORDER BY product_id;