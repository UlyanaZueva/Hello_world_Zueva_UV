import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------
# БЛОК 1: ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ
# -----------------------------------------------------------------------------

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5435",
        user="postgres_task",
        password="student",
        database="student"
    )
    print("✓ Подключение к базе данных установлено")

    # --- Запрос 1: Цены товаров по категориям ---
    df_prices = pd.read_sql("""
        SELECT 
            p.name AS product_name,
            p.category AS category,
            pr.price AS price
        FROM prices pr
        JOIN products p ON pr.product_id = p.id
    """, connection)

    # --- Запрос 2: Статистика по категориям ---
    df_categories = pd.read_sql("""
        SELECT 
            category,
            COUNT(*) AS product_count,
            ROUND(AVG(price)::numeric, 2) AS avg_price,
            MIN(price) AS min_price,
            MAX(price) AS max_price
        FROM (
            SELECT p.category, pr.price
            FROM prices pr
            JOIN products p ON pr.product_id = p.id
        ) AS subquery
        GROUP BY category
        ORDER BY product_count DESC
    """, connection)

    # --- Запрос 3: Все цены для гистограммы ---
    df_all_prices = pd.read_sql("SELECT price FROM prices", connection)

    print(f"Товаров в выборке: {len(df_prices)}")
    print(f"Категорий: {len(df_categories)}")

except Exception as error:
    print(f"Ошибка подключения: {error}")
    raise SystemExit

finally:
    connection.close()
    print("✓ Соединение закрыто\n")

# -----------------------------------------------------------------------------
# БЛОК 2: РАСЧЁТ СТАТИСТИК
# -----------------------------------------------------------------------------

mean_price = df_all_prices['price'].mean()
median_price = df_all_prices['price'].median()
std_price = df_all_prices['price'].std()

# Поиск выбросов методом IQR
Q1 = df_all_prices['price'].quantile(0.25)
Q3 = df_all_prices['price'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Аномалии (выбросы) - цены за пределами 1.5*IQR
outliers = df_all_prices[(df_all_prices['price'] < lower_bound) |
                          (df_all_prices['price'] > upper_bound)]

# Самая яркая аномалия - максимальная цена (самый дорогой товар)
max_price_outlier = df_all_prices['price'].max()
max_price_row = df_all_prices[df_all_prices['price'] == max_price_outlier].iloc[0] if len(outliers) > 0 else None

print("📊 Статистика цен:")
print(f"   Среднее: {mean_price:.2f}")
print(f"   Медиана: {median_price:.2f}")
print(f"   Нормальный диапазон: [{lower_bound:.0f} - {upper_bound:.0f}]")
print(f"   Аномалий (выбросов): {len(outliers)} шт.")
if max_price_row is not None:
    print(f"   Самая яркая аномалия: цена {max_price_outlier:.2f}")
print()

# -----------------------------------------------------------------------------
# БЛОК 3: ПОСТРОЕНИЕ ГРАФИКОВ
# -----------------------------------------------------------------------------

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
fig.suptitle("Анализ товаров и цен", fontsize=18, fontweight="bold")

# =============================================================================
# ГРАФИК 1: Количество товаров по категориям (БЕЗ аномалий - просто диаграмма)
# =============================================================================
ax1 = axes[0, 0]

categories = df_categories['category'].tolist()
counts = df_categories['product_count'].tolist()

bars1 = ax1.bar(categories, counts, color='steelblue', edgecolor='white', linewidth=1.5)

for bar, val in zip(bars1, counts):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             str(val), ha='center', va='bottom', fontweight='bold')

ax1.set_xlabel("Категория", fontsize=11)
ax1.set_ylabel("Количество товаров", fontsize=11)
ax1.set_title("1. Количество товаров по категориям", fontweight="bold")
ax1.tick_params(axis='x', rotation=20)
ax1.grid(axis='y', alpha=0.3)

# =============================================================================
# ГРАФИК 2: Диапазон цен по категориям (С АНОМАЛИЕЙ - самый дорогой товар)
# =============================================================================
ax2 = axes[0, 1]

# Сортируем по средней цене
df_sorted = df_categories.sort_values('avg_price')
cats_sorted = df_sorted['category'].tolist()
mins = df_sorted['min_price'].tolist()
avgs = df_sorted['avg_price'].tolist()
maxs = df_sorted['max_price'].tolist()

y_pos = range(len(cats_sorted))

# Рисуем линии от минимума до максимума
for i, (mn, mx) in enumerate(zip(mins, maxs)):
    ax2.plot([mn, mx], [i, i], color='lightgray', linewidth=8, zorder=1)

# Маркеры
ax2.scatter(mins, y_pos, color='green', marker='o', s=80, label='Минимум', zorder=3)
ax2.scatter(maxs, y_pos, color='red', marker='o', s=80, label='Максимум', zorder=3)
ax2.scatter(avgs, y_pos, color='blue', marker='D', s=100, label='Среднее', zorder=4)

# Подписи значений
for i, (mn, avg, mx) in enumerate(zip(mins, avgs, maxs)):
    ax2.text(mn - max(maxs)*0.02, i, f'{mn:.0f}', va='center', ha='right', fontsize=8)
    ax2.text(mx + max(maxs)*0.02, i, f'{mx:.0f}', va='center', ha='left', fontsize=8)
    ax2.text(avg, i + 0.2, f'{avg:.0f}', va='bottom', ha='center', fontsize=9, fontweight='bold')

# АНОМАЛИЯ (ВЫБРОС) - самый дорогой товар
if max_price_row is not None:
    # Находим категорию этого товара
    outlier_category = max_price_row['category'] if 'category' in max_price_row.index else cats_sorted[0]
    # Рисуем красную звездочку на графике 2 (на максимальной цене)
    for i, cat in enumerate(cats_sorted):
        if cat == outlier_category and max_price_outlier <= maxs[i]:
            ax2.scatter(max_price_outlier, i, color='red', marker='*', s=300,
                       zorder=5, edgecolor='black', linewidth=1,
                       label=f'Аномалия: {max_price_outlier:.0f}')
            ax2.annotate(
                f'⚠ АНОМАЛИЯ (ВЫБРОС)\nСамый дорогой товар\n{max_price_outlier:.0f}',
                xy=(max_price_outlier, i),
                xytext=(max_price_outlier * 0.6, i - 0.5),
                arrowprops={'arrowstyle': '->', 'color': 'red', 'lw': 1.5},
                fontsize=8, color='red', fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
            )
            break

ax2.set_yticks(y_pos)
ax2.set_yticklabels(cats_sorted, fontsize=10)
ax2.set_xlabel("Цена", fontsize=11)
ax2.set_title("2. Диапазон цен по категориям", fontweight="bold")
ax2.legend(loc='lower right', fontsize=8)
ax2.grid(axis='x', alpha=0.3)

# =============================================================================
# ГРАФИК 3: Гистограмма распределения всех цен (с выделением аномалий)
# =============================================================================
ax3 = axes[1, 0]

n, bins, patches = ax3.hist(df_all_prices['price'], bins=20,
                             color='steelblue', edgecolor='white', alpha=0.7)

# Линии среднего и медианы
ax3.axvline(mean_price, color='red', linestyle='-', linewidth=2, label=f'Среднее = {mean_price:.0f}')
ax3.axvline(median_price, color='green', linestyle='--', linewidth=2, label=f'Медиана = {median_price:.0f}')

# Вертикальные линии границ нормы
ax3.axvline(lower_bound, color='orange', linestyle=':', linewidth=1.5, alpha=0.7, label=f'Нижняя граница нормы')
ax3.axvline(upper_bound, color='orange', linestyle=':', linewidth=1.5, alpha=0.7, label=f'Верхняя граница нормы')

# Выделяем аномалию (самый дорогой товар)
if max_price_row is not None:
    ax3.annotate(
        f'⚠ АНОМАЛИЯ (ВЫБРОС)\nСамый дорогой товар\n{max_price_outlier:.0f}',
        xy=(max_price_outlier, 1),
        xytext=(max_price_outlier - max_price_outlier*0.3, n.max() * 0.7),
        arrowprops={'arrowstyle': '->', 'color': 'red', 'lw': 1.5},
        fontsize=9, color='red', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
    )

ax3.set_xlabel("Цена", fontsize=11)
ax3.set_ylabel("Количество товаров", fontsize=11)
ax3.set_title("3. Распределение цен (★ аномалия — выброс)", fontweight="bold")
ax3.legend(fontsize=8)
ax3.grid(axis='y', alpha=0.3)

stats_text = f"n = {len(df_all_prices)}\nСр = {mean_price:.0f}\nМедиана = {median_price:.0f}\nНорма: {lower_bound:.0f}–{upper_bound:.0f}"
ax3.text(0.95, 0.95, stats_text, transform=ax3.transAxes,
         va='top', ha='right', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

# =============================================================================
# ГРАФИК 4: Средняя цена по категориям
# =============================================================================
ax4 = axes[1, 1]

df_sorted_avg = df_categories.sort_values('avg_price')
cats_avg = df_sorted_avg['category'].tolist()
avgs_only = df_sorted_avg['avg_price'].tolist()

y_pos = range(len(cats_avg))

bars4 = ax4.barh(y_pos, avgs_only, color='coral', edgecolor='white', linewidth=1.5, height=0.6)

for bar, val in zip(bars4, avgs_only):
    ax4.text(bar.get_width() + max(avgs_only)*0.02,
             bar.get_y() + bar.get_height()/2,
             f'{val:.0f}', va='center', fontweight='bold')

ax4.axvline(mean_price, color='red', linestyle='--', linewidth=2, label=f'Общее среднее = {mean_price:.0f}')
ax4.set_yticks(y_pos)
ax4.set_yticklabels(cats_avg, fontsize=10)
ax4.set_xlabel("Средняя цена", fontsize=11)
ax4.set_title("4. Средняя цена по категориям", fontweight="bold")
ax4.legend(fontsize=9)
ax4.grid(axis='x', alpha=0.3)

# -----------------------------------------------------------------------------
# БЛОК 4: АНАЛИЗ АНОМАЛИЙ (ВЫБРОСОВ)
# -----------------------------------------------------------------------------

print("\n" + "="*60)
print("🔍 АНАЛИЗ АНОМАЛИЙ (ВЫБРОСОВ) В ДАННЫХ")
print("="*60)

# Настоящие выбросы
if len(outliers) > 0:
    print(f"\n⚠ ОБНАРУЖЕНЫ ВЫБРОСЫ (аномальные цены): {len(outliers)} шт.")
    print(f"   Нормальный диапазон: [{lower_bound:.0f} - {upper_bound:.0f}]")
    print("\n   Список аномалий:")
    for idx, row in outliers.iterrows():
        print(f"     - Цена: {row['price']:.2f}")
else:
    print("\n Выбросов (аномалий) не обнаружено")

# Самая яркая аномалия
if max_price_row is not None:
    print(f"\n⭐ САМАЯ ЯРКАЯ АНОМАЛИЯ:")
    print(f"   Цена: {max_price_outlier:.2f}")
    if 'product_name' in max_price_row.index:
        print(f"   Товар: {max_price_row['product_name']}")
    if 'category' in max_price_row.index:
        print(f"   Категория: {max_price_row['category']}")

# -----------------------------------------------------------------------------
# БЛОК 5: СОХРАНЕНИЕ
# -----------------------------------------------------------------------------

plt.tight_layout()
plt.savefig("task_7_data_analysis.png", dpi=150, bbox_inches="tight")
print("\n✓ График сохранён: task_7_data_analysis.png")
plt.show()

# -----------------------------------------------------------------------------
# БЛОК 6: ВЫВОДЫ
# -----------------------------------------------------------------------------

print("\n" + "="*60)
print("📈 ВЫВОДЫ ПО РЕЗУЛЬТАТАМ АНАЛИЗА")
print("="*60)

print(f"""
1. ГРАФИК 1 (Количество товаров):
   → Самая популярная категория: {categories[counts.index(max(counts))]} ({max(counts)} товаров)
   → Самая малочисленная категория: {categories[counts.index(min(counts))]} ({min(counts)} товаров)

2. ГРАФИК 2 (Диапазон цен):
   → ★ АНОМАЛИЯ (ВЫБРОС): самый дорогой товар — {max_price_outlier:.2f}
   → Выделен красной звездой и аннотацией

3. ГРАФИК 3 (Распределение цен):
   → Средняя цена: {mean_price:.2f}
   → Медианная цена: {median_price:.2f}
   → Нормальный диапазон (1.5×IQR): {lower_bound:.0f} – {upper_bound:.0f}
   → ★ Аномалия (выброс) выделена стрелкой

4. ГРАФИК 4 (Средняя цена по категориям):
   → Самая дорогая категория: {df_categories.loc[df_categories['avg_price'].idxmax(), 'category']} ({max(df_categories['avg_price']):.0f})
   → Самая бюджетная: {df_categories.loc[df_categories['avg_price'].idxmin(), 'category']} ({min(df_categories['avg_price']):.0f})

5. АНОМАЛИИ (ВЫБРОСЫ):
   → Всего выбросов: {len(outliers)} шт.
""")