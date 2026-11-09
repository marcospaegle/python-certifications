"""5.1.2 - csv.reader / csv.writer.

Reads people.csv and sales.csv (next to this script); writes and deletes _totals.csv.
"""
import csv
import os

with open("people.csv", newline="", encoding="utf-8") as f:
    for row in csv.reader(f):
        print(row)
# -> ['name', 'age', 'city']
# -> ['Ada', '36', 'London']
# -> ['Alan', '41', 'Wilmslow, Cheshire']

# The naive split breaks the quoted field
with open("people.csv", encoding="utf-8") as f:
    print(f.readlines()[2].strip().split(","))  # -> ['Alan', '41', '"Wilmslow', ' Cheshire"']

with open("people.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    total_age = 0
    for name, age, city in reader:
        total_age += int(age)
print(header, total_age)           # -> ['name', 'age', 'city'] 77

totals = {}
with open("sales.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    for region, amount in reader:
        totals[region] = totals.get(region, 0) + int(amount)
print(totals)                      # -> {'north': 150, 'south': 250}

with open("_totals.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["region", "total"])
    writer.writerows(totals.items())      # each (region, total) tuple is one row
    writer.writerow(["note", "contains, comma"])

with open("_totals.csv", newline="", encoding="utf-8") as f:
    print(repr(f.read()))          # -> 'region,total\r\nnorth,150\r\nsouth,250\r\nnote,"contains, comma"\r\n'

os.remove("_totals.csv")
