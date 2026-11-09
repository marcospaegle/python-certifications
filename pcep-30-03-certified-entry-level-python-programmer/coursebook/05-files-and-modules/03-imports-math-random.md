# 5.2 Modules and Imports: `math` and `random`

**Objectives covered:** `5.2.1`, `5.2.2`, `5.2.3`
**Exam section:** 5 – File Handling and Module Imports

### What the exam expects (official syllabus, paraphrased)
- [ ] **5.2.1** – The purpose and benefits of importing existing code
- [ ] **5.2.1** – `import` a module; access its objects
- [ ] **5.2.2** – `ceil()` rounds up, `floor()` rounds down, `trunc()` drops the fraction, `sqrt()`
- [ ] **5.2.3** – `random()` floats; `seed()` and repeatable results
- [ ] **5.2.3** – `choice()` picks one element; `sample()` picks multiple unique elements

---

## 1. Modules and the `import` keyword (5.2.1)

A **module** is a `.py` file (or a built-in compiled module) containing definitions: functions, constants and classes.

Why import existing code:
- **Reuse:** don't reimplement solved problems. Python's **standard library** ships with the interpreter, with modules such as `math`, `random` and `csv`.
- **Reliability:** library code is widely used and tested.
- **Organization:** code is split into separate namespaces, so names in different modules don't clash (`math.floor` vs your own `floor`).
- **Productivity:** less code to write and maintain.

After `import math`, the module's objects are accessed with **dot notation**: `math.sqrt`, `math.pi`.

Importing runs the module's top-level code **once per program**. Later imports reuse the cached module.

### Forms of import

```python
import math                       # binds the name `math`; access members via math.sqrt
print(math.sqrt(16))              # 4.0

import math as m                  # alias
print(m.pi)                       # 3.141592653589793

from math import sqrt, pi         # binds sqrt and pi directly; `math` itself is NOT bound
print(sqrt(9))                    # 3.0
print(math.floor(2.5))            # NameError if only `from math import ...` was used

from math import sqrt as square_root   # alias for a member
from math import *                # imports all public names: discouraged (pollutes the namespace, shadows names)
```

| Statement | Names created in your namespace |
|---|---|
| `import math` | `math` |
| `import math as m` | `m` (not `math`) |
| `from math import sqrt` | `sqrt` (not `math`) |
| `from math import sqrt as s` | `s` |
| `from math import *` | every public name in `math` |

Exploring a module:

```python
import math
print(dir(math))          # list of names defined in math
help(math.sqrt)           # documentation
```

Importing a module that doesn't exist raises `ModuleNotFoundError` (a subclass of `ImportError`). Importing a name the module doesn't have raises `ImportError: cannot import name ...`.

A name you import can shadow, or be shadowed by, your own names:

```python
from math import pi
pi = 3                    # your pi now hides math's pi
```

## 2. `math` (5.2.2)

| Function | Meaning | Returns |
|---|---|---|
| `math.ceil(x)` | smallest integer ≥ x (rounds **up**) | `int` |
| `math.floor(x)` | largest integer ≤ x (rounds **down**) | `int` |
| `math.trunc(x)` | drops the fractional part (rounds **toward zero**) | `int` |
| `math.sqrt(x)` | square root | **`float`** always |

```python
import math

math.ceil(2.1)     # 3
math.ceil(-2.1)    # -2
math.floor(2.9)    # 2
math.floor(-2.1)   # -3
math.trunc(2.9)    # 2
math.trunc(-2.9)   # -2
math.ceil(5)       # 5     (ints pass through)

math.sqrt(16)      # 4.0   (a float, not 4)
math.sqrt(2)       # 1.4142135623730951
math.sqrt(-1)      # ValueError: math domain error
```

How they compare, for positive and negative values:

| x | `floor` | `ceil` | `trunc` | `int()` | `round()` |
|---|---|---|---|---|---|
| 2.7 | 2 | 3 | 2 | 2 | 3 |
| -2.7 | -3 | -2 | -2 | -2 | -3 |
| 2.5 | 2 | 3 | 2 | 2 | 2 (ties to even) |

Constants: `math.pi` (3.141592653589793) and `math.e` (2.718281828459045). Other functions: `math.pow(x, y)` (always returns a float), `math.factorial(n)`, `math.fabs(x)` and `math.hypot(x, y)`.

## 3. `random` (5.2.3)

The `random` module generates **pseudo-random** numbers. They come from a deterministic algorithm, the Mersenne Twister, initialized by a seed.

| Function | Returns |
|---|---|
| `random.random()` | a float in **[0.0, 1.0)**: 0.0 is possible, 1.0 never |
| `random.seed(a)` | initializes the generator; the same seed gives the same sequence |
| `random.choice(seq)` | one random element of a **non-empty sequence** (`IndexError` if it's empty) |
| `random.sample(population, k)` | a **new list** of `k` **unique** elements, chosen without replacement |

```python
import random

x = random.random()          # e.g. 0.8444218515250481; 0 <= x < 1
random.choice([10, 20, 30])  # one of the three
random.choice("abc")         # a random character
random.sample(range(1, 50), 6)   # six distinct numbers, like a lottery draw
random.sample([1, 2, 3], 3)  # a random permutation of all three
random.sample([1, 2, 3], 4)  # ValueError: Sample larger than population or is negative
```

`choice` and `sample` need a **sequence** (list, tuple, string or range). `random.sample` doesn't accept a set in Python 3.11+ (`TypeError`), so convert it with `sorted(s)` first.

### Repeatable results with `seed()`

```python
import random

random.seed(42)
a = (random.random(), random.random(), random.random())
random.seed(42)
b = (random.random(), random.random(), random.random())
print(a == b)                # True: same seed, same sequence
```

Without an explicit seed, Python seeds from the operating system's randomness or the current time, so each run differs. Seeding is how you make tests and simulations reproducible.

```python
random.seed(1)
print(random.choice(["red", "green", "blue"]))   # always the same color with seed 1
```

The exam won't ask you to predict the *specific* value produced by a seed. It asks about **properties**: ranges, uniqueness, return types, and the fact that seeding makes results repeatable.

Other functions: `random.randint(a, b)` (both ends **inclusive**), `random.randrange(start, stop, step)` (with `range` semantics) and `random.shuffle(lst)` (shuffles in place and returns `None`).

---

## Exam traps
- `from math import sqrt` doesn't bind `math`, so `math.sqrt(...)` then raises `NameError`.
- `import math as m` binds only `m`.
- `math.sqrt` always returns a float.
- `ceil` and `floor` return ints. `floor(-2.1)` is `-3`, and `trunc(-2.9)` is `-2`.
- `random.random()` never returns 1.0.
- `sample` returns unique elements, and `k` larger than the population raises `ValueError`.
- `choice([])` raises `IndexError`.
- The same seed always gives the same sequence.

## Key takeaways
- There are several import forms, and each binds a different set of names.
- From `math`, know `ceil`, `floor` and `trunc` (direction of rounding) and `sqrt` (float).
- From `random`, know `random()` (in [0, 1)), `seed()` (reproducibility), `choice()` (one element) and `sample()` (k unique elements).
