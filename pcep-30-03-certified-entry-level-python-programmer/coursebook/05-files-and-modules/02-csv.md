# 5.1b CSV Files with the `csv` Module

**Objectives covered:** `5.1.2`
**Exam section:** 5 – File Handling and Module Imports

### What the exam expects (official syllabus, paraphrased)
- [ ] **5.1.2** – Basic CSV structure
- [ ] **5.1.2** – Import and use `csv`
- [ ] **5.1.2** – `csv.reader()`, `csv.writer()`
- [ ] **5.1.2** – Process rows and values

---

## 1. CSV structure

A **CSV** (comma-separated values) file is plain text:
- One **record per line**.
- **Fields** separated by a delimiter (a comma by default).
- Often a **header row** with the column names first.
- Fields that contain the delimiter, quotes or newlines are wrapped in **double quotes**. A literal quote inside a field is doubled (`""`).

```text
name,age,city
Ada,36,London
Alan,41,"Wilmslow, Cheshire"
```

Splitting this with `line.split(",")` breaks the quoted field. The `csv` module handles the quoting correctly, which is why it exists.

## 2. Reading with `csv.reader()`

```python
import csv

with open("people.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['name', 'age', 'city']
# ['Ada', '36', 'London']
# ['Alan', '41', 'Wilmslow, Cheshire']
```

- `csv.reader(file)` returns an iterator. **Each row is a list of strings.**
- **Every field is a `str`**, even numbers: convert them with `int()` or `float()`.
- The header row is just the first row. Skip or capture it with `next(reader)`:

```python
with open("people.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)          # ['name', 'age', 'city']
    total_age = 0
    for name, age, city in reader: # unpack each row
        total_age += int(age)
print(total_age)                   # 77
```

- Open CSV files with **`newline=""`**, as the `csv` documentation recommends. The csv module handles line endings itself, and this prevents blank lines or broken quoted newlines.
- Other delimiters: `csv.reader(f, delimiter=";")`.
- An empty line in the file comes out as an empty list `[]`.

## 3. Writing with `csv.writer()`

```python
import csv

rows = [
    ["name", "age", "city"],
    ["Ada", 36, "London"],
    ["Alan", 41, "Wilmslow, Cheshire"],
]
with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["product", "price"])  # one row (any iterable)
    writer.writerows(rows)                 # many rows (an iterable of iterables)
```

- `writerow(iterable)` writes one line. Non-string values are converted with `str()`, so `36` is written as `36`.
- `writerows(list_of_rows)` writes several lines.
- Fields that contain the delimiter are **quoted automatically**: `Wilmslow, Cheshire` is written as `"Wilmslow, Cheshire"`.
- Line terminator: by default the writer ends rows with `\r\n`, which is the CSV standard. Without `newline=""` you get `\r\r\n` (blank lines) on Windows.

## 4. Processing rows: a full example

`sales.csv`:

```text
region,amount
north,100
south,250
north,50
```

```python
import csv

totals = {}
with open("sales.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)                                   # skip the header
    for region, amount in reader:
        totals[region] = totals.get(region, 0) + int(amount)

print(totals)          # {'north': 150, 'south': 250}

with open("totals.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["region", "total"])
    for region, total in totals.items():
        writer.writerow([region, total])
```

(`csv.DictReader` and `csv.DictWriter`, which map rows to dicts keyed by the header, exist too, but the syllabus names only `reader` and `writer`.)

---

## Exam traps
- `csv.reader` yields lists of **strings**, so `row[1] + 1` raises a `TypeError`. Convert first.
- The header is an ordinary row unless you skip it with `next(reader)`.
- Quoted fields can contain commas, which `split(",")` gets wrong.
- `writerow` takes **one** iterable (a list), not separate arguments. `writerow("abc")` writes `a,b,c`, because a string is an iterable of characters.
- Open CSV files with `newline=""`.

## Key takeaways
- `csv.reader(f)` gives one list of strings per line.
- `csv.writer(f)` provides `.writerow(row)` and `.writerows(rows)`.
- Convert types yourself, and handle the header row explicitly.
