--Выведите список цен товаров, используя алиасы таблиц: 
--products → p 
--prices → pr 
--В результате нужно вывести: "название товара"  "цену"
SELECT 
p.name,
pr.price
FROM products as p
JOIN prices as pr ON p.id = pr.product_id;