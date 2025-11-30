import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
filename2 = 'data/sample.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
with open(filename2) as f2:
    a = csv.reader(f2)
    a_row = next(f2)
    print(a_row)