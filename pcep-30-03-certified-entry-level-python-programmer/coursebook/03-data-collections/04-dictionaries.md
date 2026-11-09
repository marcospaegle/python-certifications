# 3.4 Dictionaries

**Objectives covered:** `3.4.1`
**Exam section:** 3 – Data Collections

### What the exam expects (official syllabus, paraphrased)
- [ ] **3.4.1** – Create empty and populated dicts
- [ ] **3.4.1** – Access values by key; `in` / `not in` to test for keys
- [ ] **3.4.1** – Add new pairs and update existing values
- [ ] **3.4.1** – Remove pairs
- [ ] **3.4.1** – Iterate with `keys()`, `values()`, `items()`

---

A `dict` is a **mutable mapping from unique, hashable keys to values**. Since Python 3.7, dicts **preserve insertion order**.

## 1. Creation

```python
empty = {}
empty2 = dict()
ages = {"ann": 30, "bob": 25}
mixed = {1: "one", "two": 2, (3, 4): [5]}   # keys of different hashable types
from_pairs = dict([("a", 1), ("b", 2)])
from_kw = dict(a=1, b=2)                     # {'a': 1, 'b': 2}
```

- **Keys** must be hashable (str, int, float, bool, tuple of hashables). `{[1]: "x"}` raises `TypeError: unhashable type: 'list'`.
- **Values** can be anything.
- **Duplicate keys:** the last one wins: `{"a": 1, "a": 2}` is `{'a': 2}`.
- `1`, `1.0` and `True` are the same key: `{1: "x", True: "y"}` is `{1: 'y'}`.

## 2. Access and membership by key

```python
ages = {"ann": 30, "bob": 25}
ages["ann"]          # 30
ages["zoe"]          # KeyError: 'zoe'
ages.get("zoe")      # None    (no error)
ages.get("zoe", 0)   # 0       (default)

"ann" in ages        # True   (membership checks KEYS)
"zoe" not in ages    # True
30 in ages           # False  (values aren't checked)
30 in ages.values()  # True
len(ages)            # 2
```

Safe-access pattern: test first, then index:

```python
key = "zoe"
if key in ages:
    print(ages[key])
else:
    print(key, "not found")    # zoe not found
```

There's no positional indexing: `ages[0]` looks up the **key** `0`, and raises `KeyError` here.

## 3. Adding and updating

Assigning to a key **adds it if absent, and replaces its value if present**:

```python
ages = {"ann": 30}
ages["bob"] = 25       # add    -> {'ann': 30, 'bob': 25}
ages["ann"] = 31       # update -> {'ann': 31, 'bob': 25}  (position kept)
ages.update({"cid": 40, "bob": 26})   # merge, overwriting existing keys
```

Counting pattern:

```python
counts = {}
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1
print(counts)          # {'b': 1, 'a': 3, 'n': 2}
```

## 4. Removing

| Operation | Effect | Missing key |
|---|---|---|
| `del d[k]` | removes key `k` | `KeyError` |
| `d.pop(k)` | removes `k` and returns its value | `KeyError` |
| `d.pop(k, default)` | as above, returning `default` if `k` is missing | no error |
| `d.popitem()` | removes and returns the **last inserted** `(key, value)` pair | `KeyError` if empty |
| `d.clear()` | removes everything | — |

```python
d = {"a": 1, "b": 2, "c": 3}
del d["a"]           # {'b': 2, 'c': 3}
v = d.pop("b")       # v = 2, d = {'c': 3}
d.pop("zzz", None)   # None, no error
```

**Don't add or remove keys while iterating over a dict.** It raises `RuntimeError: dictionary changed size during iteration`.

## 5. Iteration: `keys()`, `values()`, `items()`

```python
prices = {"apple": 1.5, "pear": 2.0}

for k in prices:               # iterating a dict yields KEYS
    print(k)                   # apple, pear

for k in prices.keys():        # same as above, explicitly
    print(k)

for v in prices.values():
    print(v)                   # 1.5, 2.0

for k, v in prices.items():    # (key, value) tuples, unpacked
    print(k, "->", v)          # apple -> 1.5 / pear -> 2.0
```

- `keys()`, `values()` and `items()` return **view objects**. They're iterable and support `len` and `in` (on keys and items), but **not indexing**. Wrap them in `list()` to get a list:

```python
print(prices.keys())           # dict_keys(['apple', 'pear'])
print(list(prices.items()))    # [('apple', 1.5), ('pear', 2.0)]
print(sorted(prices))          # ['apple', 'pear']  (sorted keys)
```

Nested dictionaries:

```python
users = {"ann": {"age": 30, "langs": ["py"]}}
users["ann"]["age"]            # 30
users["ann"]["langs"].append("sql")
```

---

## Exam traps
- `d[missing]` raises `KeyError`, while `d.get(missing)` returns `None`.
- `in` checks keys, not values.
- Iterating a dict directly gives you its keys.
- A duplicate key in a literal means the last value wins.
- `{}` is an empty dict, not a set.
- `d[0]` is a key lookup, not a position.
- Updating an existing key keeps its original insertion position.
- `popitem()` removes the most recently inserted pair.

## Key takeaways
- A dict is an insertion-ordered mapping with unique, hashable keys.
- `d[k] = v` adds or updates; `del`, `pop` and `popitem` remove.
- Iterate with `keys()`, `values()`, or `items()` with tuple unpacking.
