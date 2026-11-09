# 2.2b `for` Loops and `range()`

**Objectives covered:** `2.2.2`, `2.2.3`
**Exam section:** 2 – Control Flow

### What the exam expects (official syllabus, paraphrased)
- [ ] **2.2.2** – `for` over a sequence or iterable; `in` retrieves successive elements
- [ ] **2.2.2** – Iterate strings, lists and tuples
- [ ] **2.2.2** – Process each element; trace the values of the loop variable
- [ ] **2.2.3** – `range()` for integer sequences
- [ ] **2.2.3** – start, stop and step arguments; positive and negative steps
- [ ] **2.2.3** – Trace the values `range()` produces

---

## 1. `for ... in` (2.2.2)

A Python `for` loop iterates **over the items of an iterable**. It's a "for each" loop, not a counter loop.

```python
for item in iterable:
    body
```

On each iteration the next item is assigned to the loop variable.

```python
for ch in "abc":
    print(ch)              # a, b, c

for n in [10, 20, 30]:
    print(n)               # 10, 20, 30

for x in (1, 2):
    print(x)               # 1, 2

for key in {"a": 1, "b": 2}:
    print(key)             # a, b  (iterating a dict yields its keys)

for _ in range(3):
    print("hi")            # _ means "I don't use the variable"
```

An empty iterable gives zero iterations. Strings, lists, tuples, sets, dicts and ranges are all iterable. **Integers aren't**:

```python
for i in 5:     # TypeError: 'int' object is not iterable
    ...
```

### Rebinding the loop variable doesn't affect iteration

```python
for i in range(3):
    print(i)
    i = 100        # no effect on the next iteration
# prints 0, 1, 2
```

### The loop variable survives the loop

```python
for i in range(5):
    pass
print(i)           # 4
```

If the iterable was empty, the loop variable is never assigned, and using it later raises `NameError` (unless it already existed).

### Accumulator patterns

```python
total = 0
for n in [4, 7, 1]:
    total += n
print(total)       # 12

word = ""
for ch in "abc":
    word = ch + word
print(word)        # cba
```

## 2. `range()` (2.2.3)

`range(stop)`, `range(start, stop)` and `range(start, stop, step)` produce a lazy sequence of integers.

- `start` is **inclusive** (default `0`).
- `stop` is **exclusive**: it's never produced.
- `step` defaults to `1`. It **can't be 0** (`ValueError: range() arg 3 must not be zero`).
- All arguments must be **integers**. `range(2.5)` raises `TypeError`.

```python
list(range(5))          # [0, 1, 2, 3, 4]
list(range(2, 6))       # [2, 3, 4, 5]
list(range(0, 10, 3))   # [0, 3, 6, 9]
list(range(1, 10, 2))   # [1, 3, 5, 7, 9]
list(range(5, 5))       # []        start == stop
list(range(5, 2))       # []        start > stop with a positive step
```

### Negative steps

The sequence counts **down** and stops *before* reaching `stop`:

```python
list(range(5, 0, -1))   # [5, 4, 3, 2, 1]     (0 is excluded)
list(range(5, -1, -1))  # [5, 4, 3, 2, 1, 0]
list(range(10, 0, -3))  # [10, 7, 4, 1]
list(range(0, 5, -1))   # []   start < stop with a negative step
```

### Counting the items

For a positive step, `len(range(a, b, s))` = `max(0, ceil((b - a) / s))`.

```python
len(range(0, 10, 3))   # 4  -> 0,3,6,9
len(range(1, 11))      # 10
```

### `print(range(...))`

A range object isn't a list. Printing it shows its representation:

```python
print(range(3))         # range(0, 3)
print(list(range(3)))   # [0, 1, 2]
```

### Index-based iteration

```python
word = "hey"
for i in range(len(word)):
    print(i, word[i])   # 0 h / 1 e / 2 y
```

---

## Exam traps
- `stop` is exclusive: `range(1, 5)` gives 1 to 4.
- `range(5, 0)` is empty; you need `step=-1`.
- `range(5, 0, -1)` excludes 0.
- `for` over a dict iterates its keys.
- `for i in 5` is a `TypeError`.
- Assigning to the loop variable inside the body doesn't change the iteration.
- The loop variable keeps its last value after the loop.
- `print(range(3))` shows `range(0, 3)`, not a list.

## Key takeaways
- `for` iterates over the items of any iterable.
- `range(start, stop, step)` includes `start`, excludes `stop`, and needs a non-zero integer step.
- Negative steps count down; get the sign of the step wrong and the range is empty.
