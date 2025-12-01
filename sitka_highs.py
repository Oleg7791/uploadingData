import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
filename2 = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for k, column_header in enumerate(header_row):
        print(k, column_header)
with open(filename2) as f2:
    read = csv.reader(f2)
    head_row = next(read)


    # чтение дат и максимальных температур
    dates, highs, lows, precips = [], [], [],[]
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        precip = float(row[3])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        precips.append(precip)

    for row2 in read:


# нанесение данных на диаграмму
plt.style.use('classic')
fig, ax = plt.subplots()
#ax.plot(dates, highs, c='red', alpha=0.5)
#ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plot(dates, precips, c='green', alpha=0.5)
#plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# форматирование диаграммы
#plt.title('Daile high and low temperatures - 2018', fontsize=24)
plt.title('The amount of daily the amount of \ndaily precipitation Sitka - 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
#plt.ylabel('Temperature (F)', fontsize=16)
plt.ylabel('Precipitation (mm)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
