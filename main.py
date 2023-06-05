import matplotlib.pyplot as plt
import pandas as pd

months = pd.date_range(start='2023-01-01', periods=12, freq='M')
# Создаем пример данных
data = pd.DataFrame({
    'x': range(1, 13),
    'y1': [56, 67, 72, 65, 75, 96, 70, 63, 68, 100, 88, 64],
    'y2': [74, 80, 77, 56, 50, 71, 66, 91, 91, 68, 95, 79]
})
plt.subplots(figsize=(10, 4))
month_names = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']
# Создаем парные графики
plt.plot(data['x'], data['y1'], 'go', label='Факт', marker='o', linestyle='-', linewidth=2)
plt.plot(data['x'], data['y2'], 'ro', marker='o', linestyle='-', linewidth=2, label='План')
for i in range(len(data)):
    plt.annotate(f"{data['y1'][i]}", (data['x'][i], data['y1'][i]), textcoords="offset points",
                 xytext=(0, 0), ha='center')
    plt.annotate(f"{data['y2'][i]}", (data['x'][i], data['y2'][i]), textcoords="offset points",
                 xytext=(0, 0), ha='center')
    if data['y1'][i] > data['y2'][i]:
        plt.plot([data['x'][i], data['x'][i]], [data['y1'][i], data['y2'][i]], '-g', alpha=0.4, linewidth=12)
    else:
        plt.plot([data['x'][i], data['x'][i]], [data['y1'][i], data['y2'][i]], '-r', alpha=0.4, linewidth=12)

plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=2)

plt.xticks(data['x'], month_names)
plt.ylim(0, 120)
plt.title('Динамика продаж(план-факт)')

plt.show()
