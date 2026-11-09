# 3.2 Tuples

**Objectives covered:** `3.2.1`
**Exam section:** 3 – Data Collections

### What the exam expects (official syllabus, paraphrased)
- [ ] **3.2.1** – Empty, single-element and multi-element tuples
- [ ] **3.2.1** – Positive and negative indexing; slicing
- [ ] **3.2.1** – Immutability; tuples vs lists and their use cases
- [ ] **3.2.1** – Nested tuples and lists; indexing into them

---

A `tuple` is an **ordered, immutable sequence**.

## 1. Creation

```python
empty = ()
empty2 = tuple()
single = (5,)        # THE COMMA makes the tuple
single2 = 5,         # also a tuple
not_tuple = (5)      # just the int 5 in parentheses
pair = (1, "a")
packed = 1, 2, 3     # parentheses are optional: "tuple packing"
from_list = tuple([1, 2])   # (1, 2)
from_str = tuple("ab")      # ('a', 'b')
```

```python
print(type((5)))     # <class 'int'>
print(type((5,)))    # <class 'tuple'>
print(len(()))       # 0
```

## 2. Indexing and slicing

These work exactly as they do for lists, and slicing returns a new tuple:

```python
t = (10, 20, 30, 40)
t[0]       # 10
t[-1]      # 40
t[1:3]     # (20, 30)
t[::-1]    # (40, 30, 20, 10)
t[10]      # IndexError: tuple index out of range
```

Other read-only operations: `len(t)`, `x in t`, `t.index(x)`, `t.count(x)`, `t + t2`, `t * 2`, `sorted(t)` (which returns a **list**), `min`, `max`, `sum`, and iteration.

## 3. Immutability

You can't add, remove or replace elements:

```python
t = (1, 2, 3)
t[0] = 99      # TypeError: 'tuple' object does not support item assignment
t.append(4)    # AttributeError: 'tuple' object has no attribute 'append'
del t[0]       # TypeError: 'tuple' object doesn't support item deletion
```

You *can* rebind the name to a new tuple:

```python
t = (1, 2)
t = t + (3,)   # new tuple (1, 2, 3); the old one is untouched
t += (4,)      # also creates a new tuple
del t          # deleting the whole name is allowed
```

### Tuples vs lists

| | list | tuple |
|---|---|---|
| Mutable | yes | **no** |
| Syntax | `[1, 2]` | `(1, 2)` or `1, 2` |
| Methods | many (append, sort, …) | only `count`, `index` |
| Typical use | a homogeneous, changing collection | a fixed record (coordinates, return values) |
| Usable as a dict key or set element | no | yes (if all its elements are hashable) |

## 4. Nesting tuples and lists

A tuple's **references** are immutable, but the objects they point to can be mutable:

```python
t = (1, [2, 3])
t[1].append(4)     # allowed: we mutate the list, not the tuple
print(t)           # (1, [2, 3, 4])
t[1] = [9]         # TypeError: the tuple slot can't be rebound
```

Nested access:

```python
data = ((1, 2), (3, 4))
data[1][0]         # 3
points = [(0, 0), (1, 2)]   # a list of tuples
points[1] = (5, 5)          # fine: the list is mutable
```

## 5. Packing and unpacking

```python
point = (3, 4)
x, y = point            # unpacking: x=3, y=4
a, b = b, a             # swap uses packing and unpacking
for name, age in [("Ann", 30), ("Bob", 25)]:
    print(name, age)
```

The number of names must match the number of elements, or you get a `ValueError`.

---

## Exam traps
- `(5)` is an int; `(5,)` and `5,` are tuples.
- `()` is an empty tuple, and its length is 0.
- Tuples have no `append`, `remove` or `sort` (`AttributeError`). Item assignment gives a `TypeError`.
- `t += (4,)` works, because it creates a new tuple.
- A list inside a tuple can still be mutated.
- `sorted(tuple)` returns a list.

## Key takeaways
- Tuples are ordered, immutable, and support indexing and slicing.
- The comma, not the parentheses, creates a tuple.
- Immutability is shallow: contained mutable objects can still change.
