# 2.2c Nested Loops, `break`, `continue`, `pass`

**Objectives covered:** `2.2.4`, `2.2.5`
**Exam section:** 2 – Control Flow

### What the exam expects (official syllabus, paraphrased)
- [ ] **2.2.4** – Nest loops; combine loops with conditionals
- [ ] **2.2.4** – Trace nested-loop execution order
- [ ] **2.2.4** – Process multidimensional or grouped data
- [ ] **2.2.5** – `break` terminates a loop early
- [ ] **2.2.5** – `continue` skips the rest of the current iteration
- [ ] **2.2.5** – `pass` is a placeholder for an empty block
- [ ] **2.2.5** – Trace loops that contain them

---

## 1. Nested loops (2.2.4)

The inner loop runs **completely** for each iteration of the outer loop. The total number of inner iterations is the product of the two counts.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
# 0 0 / 0 1 / 1 0 / 1 1 / 2 0 / 2 1   -> 3 * 2 = 6 lines
```

The inner range can depend on the outer variable:

```python
for i in range(1, 4):
    print("*" * i)
# *
# **
# ***

count = 0
for i in range(4):
    for j in range(i):
        count += 1
print(count)    # 0 + 1 + 2 + 3 = 6
```

Combining loops with conditionals:

```python
for n in range(2, 10):
    is_prime = True
    for d in range(2, n):
        if n % d == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")    # 2 3 5 7
print()
```

### Processing multidimensional or grouped data

The outer loop walks the groups (rows) and the inner loop walks each group's items:

```python
matrix = [[1, 2, 3], [4, 5, 6]]
total = 0
for row in matrix:
    for value in row:
        total += value
print(total)            # 21

scores = {"ann": [8, 9], "bob": [6, 7, 5]}   # grouped data
for name, marks in scores.items():
    best = 0
    for m in marks:
        if m > best:
            best = m
    print(name, best)   # ann 9 / bob 7
```

Index-based nested loops, when you need positions (for example to modify cells):

```python
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        matrix[r][c] *= 10
print(matrix)           # [[10, 20, 30], [40, 50, 60]]
```

Building a multiplication table:

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end="\t")
    print()     # newline after each row
```

## 2. `break` (2.2.5)

`break` **immediately exits the innermost enclosing loop**. The rest of the body is skipped, and so are any remaining iterations.

```python
for n in [3, 8, -1, 5]:
    if n < 0:
        break
    print(n)        # 3, 8
print("after")
```

In nested loops, `break` exits **only the inner loop**. The outer loop continues:

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
# 0 0 / 1 0 / 2 0
```

`break` (and `continue`) outside a loop is a `SyntaxError`.

## 3. `continue` (2.2.5)

`continue` skips the **rest of the current iteration** and jumps to the next one. In a `for` it takes the next item; in a `while` it re-evaluates the condition.

```python
for n in range(6):
    if n % 2 == 0:
        continue
    print(n)        # 1, 3, 5
```

**Infinite loop trap with `while` and `continue`:** if the increment comes *after* the `continue`, it's skipped:

```python
i = 0
while i < 5:
    if i == 2:
        continue    # i stays 2 forever
    i += 1
```

## 4. `pass` (2.2.5)

`pass` does **nothing**. It's a syntactic placeholder wherever a statement is required but no action is wanted:

```python
for i in range(3):
    pass            # the loop runs 3 times and does nothing

if x > 0:
    pass            # TODO
else:
    print("non-positive")
```

`pass` doesn't affect control flow. It isn't `continue`: code after `pass` in the same block still runs.

```python
for i in range(2):
    pass
    print(i)        # 0, 1  (still printed)
```

## 5. Loop `else` clause *(beyond the syllabus)*

Both `for` and `while` can have an `else` block. It runs **when the loop finishes normally**, meaning it exhausts the iterable or the condition becomes false. It does **not** run when the loop exits via `break`.

```python
for n in [1, 3, 5]:
    if n % 2 == 0:
        print("found even")
        break
else:
    print("no even number")   # printed: the loop finished without break

i = 0
while i < 3:
    i += 1
else:
    print("done", i)          # done 3
```

An empty iterable still runs the `else` (zero iterations is a normal finish):

```python
for x in []:
    print(x)
else:
    print("else runs")        # printed
```

---

## Exam traps
- `break` leaves only the innermost loop.
- Loop `else` runs unless the loop ended with `break`, including when the loop had zero iterations.
- A `continue` before the increment in a `while` loop can cause an infinite loop.
- `pass` doesn't skip anything.
- To count nested iterations, multiply (or sum, when the inner range depends on the outer variable).

## Key takeaways
- The inner loop runs fully on each outer iteration.
- `break` exits the loop, `continue` moves to the next iteration, and `pass` does nothing.
- `else` on a loop means "no `break` happened".
