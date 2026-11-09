# 4.1c Scope

**Objectives covered:** `4.1.5`
**Exam section:** 4 – Functions and Exceptions

### What the exam expects (official syllabus, paraphrased)
- [ ] **4.1.5** – Local vs global scope
- [ ] **4.1.5** – How names inside a function are resolved
- [ ] **4.1.5** – Namespaces and shadowing
- [ ] **4.1.5** – `global` to modify a global from inside a function
- [ ] **4.1.5** – Risks of excessive globals

---

## 1. Local and global scope

- A name assigned at the **top level of a module** (a script) is **global**. It's visible everywhere in that module, including inside functions (for reading).
- A name assigned **inside a function**, including its parameters, is **local** to that call. It's created when the call starts and disappears when the call returns.

```python
rate = 0.2            # global

def tax(amount):      # amount is local
    result = amount * rate   # result is local; rate is READ from the global scope
    return result

print(tax(100))       # 20.0
print(result)         # NameError: name 'result' is not defined
```

Only **functions** (plus classes and modules) create scopes. `if`, `for`, `while` and `try` blocks **don't**:

```python
for i in range(3):
    inside = i
print(i, inside)      # 2 2   (both still exist)
```

### Namespaces

A **namespace** is a mapping from names to objects. Each scope has its own:
- the **built-in** namespace (`print`, `len`, …), created when Python starts
- the **global** namespace of a module, created when the module runs
- a **local** namespace for each function *call*, created at the start of the call and discarded when it returns

The same name can exist independently in different namespaces. That's what makes shadowing possible.

```python
x = "global"
def f():
    x = "local"         # a different x, in f's local namespace
    return x
print(f(), x)           # local global
```

## 2. Name resolution: LEGB

When Python looks up a name, it searches these scopes in order:
1. **L**ocal: the current function.
2. **E**nclosing: any enclosing functions (for nested functions).
3. **G**lobal: the module's top level.
4. **B**uilt-in: `print`, `len`, `range`, and so on.

The first match wins. If there's no match, you get `NameError`.

## 3. Shadowing

Assigning to a name inside a function creates a **new local variable** that hides (shadows) the global one. The global is unchanged:

```python
x = 10

def f():
    x = 99          # a new LOCAL x
    print("in f:", x)

f()                 # in f: 99
print("global:", x) # global: 10
```

Parameters shadow globals too:

```python
x = 1
def g(x):
    x = x + 1
    return x
print(g(5), x)      # 6 1
```

### `UnboundLocalError`

**If a function assigns to a name *anywhere* in its body, that name is local throughout the whole function**. This is decided at compile time. Reading it before the assignment fails:

```python
count = 0

def increment():
    count = count + 1     # UnboundLocalError: cannot access local variable 'count'
                          # where it is not associated with a value
increment()
```

```python
n = 5
def show():
    print(n)        # UnboundLocalError: n is local because of the line below
    n = 1
```

(`UnboundLocalError` is a subclass of `NameError`. The message above is the 3.12 wording.)

## 4. The `global` keyword

`global name` declares that assignments to `name` inside the function target the **global** variable:

```python
count = 0

def increment():
    global count
    count += 1

increment()
increment()
print(count)        # 2
```

- The `global` declaration must come **before** the name is used in that function.
- If the global doesn't exist yet, assigning to it creates it:

```python
def setup():
    global config
    config = "ready"

setup()
print(config)       # ready
```

- **Mutating** a global object doesn't need `global`. Only **rebinding** the name does:

```python
items = []
def add(x):
    items.append(x)     # fine: no assignment to the name `items`
add(1)
print(items)            # [1]
```

## 5. Risks of global variables

- **Hidden coupling:** a function's behaviour depends on state it doesn't receive as a parameter, so it's harder to reason about and test.
- **Action at a distance:** any function can change a global, so bugs are hard to trace.
- **Name clashes and shadowing confusion.**
- Prefer passing values in as parameters and returning results. Reserve module-level names for **constants** (`UPPER_CASE`).

## 6. Nested functions *(beyond the syllabus)*

An inner function can **read** variables of its enclosing function (the "E" in LEGB). Rebinding them requires `nonlocal`, which is outside the syllabus.

```python
def outer():
    msg = "hi"
    def inner():
        return msg      # read from the enclosing scope
    return inner()
print(outer())          # hi
```

---

## Exam traps
- Variables created inside a function don't exist outside it (`NameError`).
- `if`, `for` and `while` don't create scopes.
- Assigning inside a function creates a local that shadows the global, and the global is untouched.
- Reading a name and then assigning it in the same function, without `global`, raises `UnboundLocalError`.
- `global x` is needed to rebind a global, but not to mutate the object it refers to.
- Parameters are local.

## Key takeaways
- Name lookup follows LEGB: local, enclosing, global, built-in.
- Assignment makes a name local to its function unless it's declared `global`.
- Minimize globals and pass data explicitly.
