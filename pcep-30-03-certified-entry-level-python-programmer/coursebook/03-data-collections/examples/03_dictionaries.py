"""3.4.1 - Dictionaries."""

print({"a": 1, "a": 2})            # -> {'a': 2}
print({1: "x", True: "y"})         # -> {1: 'y'}
print(dict(a=1, b=2))              # -> {'a': 1, 'b': 2}

ages = {"ann": 30, "bob": 25}
print(ages["ann"], ages.get("zoe"), ages.get("zoe", 0))  # -> 30 None 0
print("ann" in ages, 30 in ages, 30 in ages.values())    # -> True False True

try:
    ages["zoe"]
except KeyError as e:
    print("KeyError", e)           # -> KeyError 'zoe'

ages = {"ann": 30}
ages["bob"] = 25
ages["ann"] = 31
print(ages)                        # -> {'ann': 31, 'bob': 25}
ages.update({"cid": 40, "bob": 26})
print(ages)                        # -> {'ann': 31, 'bob': 26, 'cid': 40}

counts = {}
for ch in "banana":
    counts[ch] = counts.get(ch, 0) + 1
print(counts)                      # -> {'b': 1, 'a': 3, 'n': 2}

d = {"a": 1, "b": 2, "c": 3}
del d["a"]
v = d.pop("b")
print(v, d, d.pop("zzz", None))    # -> 2 {'c': 3} None
d = {"x": 1, "y": 2}
print(d.popitem())                 # -> ('y', 2)

prices = {"apple": 1.5, "pear": 2.0}
for k, v in prices.items():
    print(k, "->", v)
# -> apple -> 1.5
# -> pear -> 2.0
print(prices.keys())               # -> dict_keys(['apple', 'pear'])
print(list(prices.values()))       # -> [1.5, 2.0]
print(list(prices.items()))        # -> [('apple', 1.5), ('pear', 2.0)]

users = {"ann": {"age": 30, "langs": ["py"]}}
users["ann"]["langs"].append("sql")
print(users["ann"]["age"], users["ann"]["langs"])  # -> 30 ['py', 'sql']

try:
    for k in d:
        d["new"] = 0
except RuntimeError as e:
    print(e)                       # -> dictionary changed size during iteration
