# 3.3 Sets

**Objectives covered:** `3.3.1`
**Exam section:** 3 – Data Collections

### What the exam expects (official syllabus, paraphrased)
- [ ] **3.3.1** – Defining characteristics of `set`
- [ ] **3.3.1** – Create empty and populated sets
- [ ] **3.3.1** – Why sets have no positional indexing
- [ ] **3.3.1** – Add and remove elements
- [ ] **3.3.1** – `in` / `not in`

---

A `set` is an **unordered, mutable collection of unique, hashable elements**.

## 1. Characteristics

- **Unique:** duplicates are discarded automatically.
- **Unordered:** there are no positions, so there's **no indexing or slicing**. Iteration order is arbitrary, so don't rely on it.
- **Hashable elements only:** ints, floats, strings, bools, `None` and tuples of hashables are allowed. Lists, dicts and sets aren't (`TypeError: unhashable type: 'list'`).
- **Mutable:** you can add and remove elements.
- **Fast membership tests:** `x in s` is O(1) on average.

## 2. Creation

```python
s = {1, 2, 3}
s = {3, 1, 3, 2, 1}      # {1, 2, 3}  (duplicates removed)
empty = set()            # the ONLY way to make an empty set
not_a_set = {}           # this is an empty DICT
from_list = set([1, 1, 2])   # {1, 2}
from_str = set("hello")      # {'h', 'e', 'l', 'o'} (order varies)
len({1, 1, 1})           # 1
```

```python
print(type({}))          # <class 'dict'>
print(type(set()))       # <class 'set'>
```

`True` and `1` (and `False` and `0`) are equal and hash the same, so they count as duplicates: `{1, True}` is `{1}`.

## 3. No positional access

```python
s = {10, 20, 30}
s[0]        # TypeError: 'set' object is not subscriptable
```

To access the elements, iterate (`for x in s`), test membership, or convert with `sorted(s)` or `list(s)`.

## 4. Adding and removing

| Method | Effect | If the element is missing |
|---|---|---|
| `s.add(x)` | adds one element (no-op if already present) | — |
| `s.remove(x)` | removes `x` | **`KeyError`** |
| `s.discard(x)` | removes `x` if present | silently does nothing |
| `s.pop()` | removes and returns an **arbitrary** element | `KeyError` if the set is empty |
| `s.clear()` | removes everything | — |
| `s.update(iterable)` | adds every element of the iterable | — |

```python
s = {1, 2}
s.add(3)          # {1, 2, 3}
s.add(2)          # unchanged
s.update([4, 5])  # {1, 2, 3, 4, 5}
s.discard(10)     # no error
s.remove(1)       # {2, 3, 4, 5}
s.remove(10)      # KeyError: 10
```

## 5. Membership tests

```python
vowels = {"a", "e", "i", "o", "u"}
print("e" in vowels)       # True
print("z" not in vowels)   # True
```

Deduplicating and then counting is a typical exam scenario:

```python
words = ["a", "b", "a", "c", "b"]
print(len(set(words)))     # 3
```

## 6. Set operations *(beyond the syllabus)*

These follow naturally from sets' characteristics:

```python
a, b = {1, 2, 3}, {2, 3, 4}
a | b    # {1, 2, 3, 4}  union          a.union(b)
a & b    # {2, 3}        intersection   a.intersection(b)
a - b    # {1}           difference     a.difference(b)
a ^ b    # {1, 4}        symmetric difference
```

---

## Exam traps
- `{}` is a dict. Use `set()` for an empty set.
- Sets can't be indexed (`TypeError`).
- `remove` on a missing element raises `KeyError`, while `discard` doesn't.
- Duplicates vanish: `len({1, 1, 2})` is `2`. `{1, True}` has one element.
- Lists can't be set elements (`TypeError: unhashable type`).
- Never predict a set's print order. Exam answers will use `sorted()` or `len()`.

## Key takeaways
- Sets are unique, unordered and mutable, and they hold only hashable elements.
- Use `add`, `remove` or `discard`, and `in`; there's no indexing.
- Sets are the idiomatic tool for deduplication and fast membership tests.
