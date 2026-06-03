import psycopg2
import pandas as pd

try:
    # Устанавливаем соединение
    connection = psycopg2.connect(
        host="localhost",
        port="5435",
        user="postgres_task",
        password="student",
        database="student"
    )
    print("✓ Подключение установлено\n")

except Exception as error:
    print(f"Ошибка при подключении: {error}")
    exit()

# 2. Выполните SQL-запрос с объединением таблиц prices и products (JOIN), чтобы получить для каждой записи
# о цене название товара и его категорию. Загрузите результат запроса в pandas DataFrame.
print("ШАГ 2: JOIN И ЗАГРУЗКА В DataFrame\n")
query = """
    SELECT 
        p.id as price_id,
        p.product_id,
        p.price,
        pr.name as product_name,
        pr.category
    FROM prices p
    JOIN products pr ON p.product_id = pr.id   -- product_id в prices связан с id в products
    ORDER BY pr.category, p.price
"""

df = pd.read_sql(query, connection)
print(f"Загружено записей: {len(df)}\n")
print("Первые 5 строк данных:")
print(df.head())
print("\n" + "-"*70 + "\n")

# 3. На основе столбца price рассчитайте следующие показатели: среднее значение, медиану, стандартное отклонение,
# минимальную и максимальную цену. Результаты необходимо вывести в читаемом формате с указанием единиц
# измерения (руб.).
print("ШАГ 3: Основные статистические показатели цен\n")

print(f"Среднее значение:       {df['price'].mean():.2f} руб.")
print(f"Медиана:                {df['price'].median():.2f} руб.")
print(f"Стандартное отклонение: {df['price'].std():.2f} руб.")
print(f"Минимальная цена:       {df['price'].min():.2f} руб.")
print(f"Максимальная цена:      {df['price'].max():.2f} руб.")

print("\n" + "-"*70 + "\n")

# 4. Рассчитайте первый квартиль (Q1), второй квартиль (медиану, Q2) и третий квартиль (Q3), а также межквартильный
# размах (IQR = Q3 − Q1). Выведите список товаров, цена которых превышает Q3, с указанием их категорий.
print("ШАГ 4: Квартильный анализ\n")

q1 = df['price'].quantile(0.25)
q2 = df['price'].quantile(0.50)
q3 = df['price'].quantile(0.75)
iqr = q3 - q1

print(f"Q1 (25%):     {q1:.2f} руб.")
print(f"Q2 (50%):     {q2:.2f} руб. (медиана)")
print(f"Q3 (75%):     {q3:.2f} руб.")
print(f"IQR (Q3-Q1):  {iqr:.2f} руб.")

# Товары с ценой выше Q3
high_price = df[df['price'] > q3]
print(f"\nТовары с ценой выше Q3 (> {q3:.2f} руб.): {len(high_price)} шт.")
print("\nСписок товаров:")
print(high_price[['product_name', 'category', 'price']].to_string(index=False))

print("\n" + "-"*70 + "\n")

# 5. Сгруппируйте данные по полю category и для каждой категории рассчитайте: количество записей о ценах, среднюю
# цену, медиану, стандартное отклонение. Результат отсортируйте по убыванию средней цены.
print("ШАГ 5: Статистика по категориям\n")

by_category = df.groupby('category')['price'].agg(
    count='count',
    mean='mean',
    median='median',
    std='std'
).round(2).sort_values('mean', ascending=False)

print(by_category.to_string())

print("\n" + "-"*70 + "\n")

# 6. Для каждого товара определите минимальную и максимальную зафиксированную цену и рассчитайте разницу между ними.
# Выведите пять товаров с наибольшим разбросом цен.
print("ШАГ 6: Топ-5 товаров с наибольшим разбросом цен\n")

price_range = df.groupby('product_name')['price'].agg(
    min_price='min',
    max_price='max',
    price_range=lambda x: x.max() - x.min(),
).round(2).sort_values('price_range', ascending=False).head(5)

print(price_range.to_string())


# Закрываем соединение
connection.close()
print("\nСоединение с БД закрыто")