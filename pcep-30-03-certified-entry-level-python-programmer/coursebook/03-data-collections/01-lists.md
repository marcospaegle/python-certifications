# 3.1 Lists

**Objectives covered:** `3.1.1`, `3.1.2`, `3.1.3`
**Exam section:** 3 – Data Collections (26%, 9 items, the largest section)

### What the exam expects (official syllabus, paraphrased)
- [ ] **3.1.1** – Create empty and populated lists, with same or mixed types
- [ ] **3.1.1** – Positive and negative indexes
- [ ] **3.1.1** – Slicing with start, stop and step; copying via slicing
- [ ] **3.1.2** – `append()`, `insert()`, `index()`
- [ ] **3.1.2** – Removal with methods or `del`
- [ ] **3.1.2** – `sorted()` and list sorting methods
- [ ] **3.1.2** – Iterate with `for`; initialize and update values while processing
- [ ] **3.1.2** – `in` / `not in`; `len()`
- [ ] **3.1.3** – Lists of lists for 2D (matrices) and deeper nesting for 3D (cubes)
- [ ] **3.1.3** – Access with multiple indexes; modify nested values

---

A `list` is an **ordered, mutable sequence** that can hold objects of any type, mixed freely.

## 1. Creation, indexing, slicing (3.1.1)

### Creation
```python
empty = []
nums = [10, 20, 30, 40, 50]
mixed = [1, "two", 3.0, [4, 5], None]
from_iter = list("abc")        # ['a', 'b', 'c']
from_range = list(range(3))    # [0, 1, 2]
zeros = [0] * 4                # [0, 0, 0, 0]
joined = [1, 2] + [3]          # [1, 2, 3]
```

### Indexing (positive and negative)

```text
 index:   0   1   2   3   4
        [10, 20, 30, 40, 50]
negative: -5  -4  -3  -2  -1
```

```python
nums[0]      # 10
nums[-1]     # 50  (last)
nums[-2]     # 40
nums[5]      # IndexError: list index out of range
nums[2] = 99 # lists are mutable -> [10, 20, 99, 40, 50]
```

### Slicing: `seq[start:stop:step]`

- `start` is inclusive (default: the beginning).
- `stop` is **exclusive** (default: the end).
- `step` defaults to 1. A negative step walks backwards, and then the defaults flip: start defaults to the end and stop to the beginning.
- A slice **always returns a new list** and **never raises `IndexError`**. Out-of-range bounds are clipped.

```python
nums = [10, 20, 30, 40, 50]
nums[1:3]     # [20, 30]
nums[:2]      # [10, 20]
nums[2:]      # [30, 40, 50]
nums[-2:]     # [40, 50]
nums[:-1]     # [10, 20, 30, 40]
nums[::2]     # [10, 30, 50]
nums[::-1]    # [50, 40, 30, 20, 10]  (reversed copy)
nums[3:1]     # []                     (start after stop with a positive step)
nums[3:1:-1]  # [40, 30]
nums[1:100]   # [20, 30, 40, 50]       (clipped, no error)
nums[-100:2]  # [10, 20]
```

Slice length for a positive step: `len(seq[a:b])` = `max(0, b - a)` once the bounds are clipped.

### Copying vs aliasing

```python
a = [1, 2, 3]
alias = a          # same object
copy1 = a[:]       # new list (shallow copy)
copy2 = a.copy()   # same as [:]
copy3 = list(a)    # same
a.append(4)
print(alias)       # [1, 2, 3, 4]
print(copy1)       # [1, 2, 3]
```

A **shallow** copy copies the outer list only, so nested lists are still shared:

```python
grid = [[1, 2], [3, 4]]
g2 = grid[:]
g2[0][0] = 99
print(grid)        # [[99, 2], [3, 4]]  (the inner list is shared)
```

### Slice assignment and deletion

```python
nums = [1, 2, 3, 4, 5]
nums[1:3] = ["a", "b", "c"]   # [1, 'a', 'b', 'c', 4, 5]  (lengths can differ)
nums[:] = []                  # empties the list in place
```

## 2. List methods and operations (3.1.2)

| Operation | Effect | Returns |
|---|---|---|
| `lst.append(x)` | adds `x` at the end (as **one** element) | `None` |
| `lst.insert(i, x)` | inserts `x` *before* index `i` | `None` |
| `lst.index(x)` | index of the first `x`; `ValueError` if absent | int |
| `lst.remove(x)` | removes the first `x`; `ValueError` if absent | `None` |
| `lst.pop()` / `lst.pop(i)` | removes and returns the last item (or the item at `i`); `IndexError` if empty | the item |
| `del lst[i]` / `del lst[a:b]` | statement: deletes by index or slice | — |
| `lst.sort()` | sorts **in place** | `None` |
| `sorted(lst)` | builds a **new** sorted list | list |
| `lst.reverse()` | reverses in place | `None` |
| `len(lst)` | number of elements | int |
| `x in lst`, `x not in lst` | membership test | bool |
| `lst.count(x)` | occurrences of `x` | int |
| `lst.extend(iter)` / `lst += iter` | appends each element | `None` |

```python
nums = [3, 1, 2]
nums.append([4, 5])     # [3, 1, 2, [4, 5]]   one element, a nested list
nums = [3, 1, 2]
nums.extend([4, 5])     # [3, 1, 2, 4, 5]

nums = [10, 20, 30]
nums.insert(1, 15)      # [10, 15, 20, 30]
nums.insert(100, 99)    # [10, 15, 20, 30, 99]  index past the end means append
nums.insert(-1, 0)      # [10, 15, 20, 30, 0, 99]  inserted BEFORE the last element

nums.index(20)          # 2
nums.remove(0)          # removes the value 0, not index 0
last = nums.pop()       # 99
del nums[0]             # [15, 20, 30]
del nums                # deletes the NAME; using nums now raises NameError
```

### Sorting

```python
data = [3, 1, 2]
result = data.sort()
print(result)            # None   <- classic trap
print(data)              # [1, 2, 3]

data = [3, 1, 2]
new = sorted(data)       # data unchanged; new == [1, 2, 3]
sorted(data, reverse=True)   # [3, 2, 1]
data.sort(reverse=True)      # in place, descending

sorted(["banana", "Apple", "cherry"])   # ['Apple', 'banana', 'cherry']  uppercase sorts first
sorted([3, "a"])         # TypeError: '<' not supported between instances of 'str' and 'int'
```

`sorted()` works on **any iterable** and always returns a list: `sorted("cba")` gives `['a', 'b', 'c']`.

### Iteration and other built-ins

```python
for item in nums: ...
for i in range(len(nums)): ...      # when you need indexes
sum([1, 2, 3])      # 6
max([4, 9, 2])      # 9
min([4, 9, 2])      # 2
```

### Initializing and updating values while processing a list

Typical patterns: start an accumulator before the loop and update it on each element. Or update the list's own elements through their indexes:

```python
prices = [12.5, 8.0, 20.0]
total = 0                   # initialize
largest = prices[0]
for p in prices:
    total += p              # update
    if p > largest:
        largest = p
print(total, largest)       # 40.5 20.0

evens = []                  # build a new list
for n in range(10):
    if n % 2 == 0:
        evens.append(n)
print(evens)                # [0, 2, 4, 6, 8]

nums = [1, 2, 3]
for i in range(len(nums)):
    nums[i] = nums[i] * 2   # modifies the list in place
print(nums)                 # [2, 4, 6]

for n in nums:
    n = 0                   # rebinds the loop variable only, so the list is unchanged
print(nums)                 # [2, 4, 6]
```

**Don't modify a list while iterating over it.** Removing elements shifts the indexes and skips items:

```python
nums = [1, 2, 2, 3]
for n in nums:
    if n == 2:
        nums.remove(n)
print(nums)    # [1, 2, 3]  (one 2 survived)
```

### Swapping and reversing idioms

```python
lst = [1, 2, 3, 4]
lst[0], lst[-1] = lst[-1], lst[0]   # [4, 2, 3, 1]
for i in range(len(lst) // 2):      # manual in-place reverse
    lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
```

## 3. Lists of lists: 2D and 3D structures (3.1.3)

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
matrix[1]        # [4, 5, 6]   (a row)
matrix[1][2]     # 6           (row 1, column 2)
matrix[-1][-1]   # 9
matrix[0][1] = 0 # modify one cell
len(matrix)      # 3 rows
len(matrix[0])   # 3 columns

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# column 1
col = []
for row in matrix:
    col.append(row[1])
```

3D example: `cube[layer][row][col]`.

```python
cube = [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
cube[1][0][1]    # 5
```

### The `*` replication trap

```python
bad = [[0] * 3] * 2          # two references to the SAME inner list
bad[0][0] = 1
print(bad)                   # [[1, 0, 0], [1, 0, 0]]

good = []
for _ in range(2):
    good.append([0] * 3)     # a NEW inner list on each iteration
good[0][0] = 1
print(good)                  # [[1, 0, 0], [0, 0, 0]]
```

(You'll also see the one-liner `[[0] * 3 for _ in range(2)]`, a *list comprehension*. It builds the same independent rows.)

The inner `[0] * 3` is safe because ints are immutable. Only the outer `*` is the problem.

---

## Exam traps
- `lst.sort()` returns `None`. So `x = lst.sort()` makes `x` `None`.
- `append([4, 5])` adds one element; `extend` adds two.
- `insert(-1, x)` inserts before the last element.
- `remove(x)` removes by value; `pop(i)` and `del` remove by index.
- Slices never raise `IndexError`, but indexing does.
- `b = a` is an alias, while `a[:]` is a (shallow) copy.
- `[[0]*3]*2` shares the inner list.
- `nums[::-1]` reverses; `nums[3:1]` is empty.

## Key takeaways
- Lists are ordered and mutable. Indexes run 0..n-1 or -n..-1.
- Slices produce copies, and `stop` is exclusive.
- Know each method's return value: many return `None` because they mutate in place.
