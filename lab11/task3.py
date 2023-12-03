import csv
from collections import defaultdict
import matplotlib.pyplot as plt

with open('passengers.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [(row['Month'], int(row['#Passengers'])) for row in reader]

years = sorted(set(month[:4] for month, _ in data))

months_data = defaultdict(list)

for month, passengers in data:
    months_data[month[5:]].append(passengers)

plt.figure(figsize=(12, 6))
plt.plot(years, [sum(passengers for month, passengers in data if month.startswith(year)) for year in years])
plt.title('Пассажиропоток за все время')
plt.xlabel('Года')
plt.ylabel('Количество пассажиров')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
for month, values in months_data.items():
    plt.bar(month, sum(values), label=month, color = 'blue')

plt.title('Распределение пассажиров по месяцам (1951-1955)')
plt.xlabel('Месяцы')
plt.ylabel('Количество пассажиров')
plt.show()
