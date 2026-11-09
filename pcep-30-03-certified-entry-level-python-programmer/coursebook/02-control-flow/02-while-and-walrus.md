# 2.2a `while` Loops and the Walrus Operator

**Objectives covered:** `2.2.1`
**Exam section:** 2 – Control Flow

### What the exam expects (official syllabus, paraphrased)
- [ ] **2.2.1** – `while` repeats while its condition is true
- [ ] **2.2.1** – Initialize and update loop-control variables (sentinel values)
- [ ] **2.2.1** – Trace condition-controlled loops
- [ ] **2.2.1** – Recognize conditions that cause infinite loops
- [ ] **2.2.1** – Use the walrus operator `:=` where appropriate

---

## 1. `while`

```python
while condition:
    body
```

The condition is evaluated **before each iteration**. While it's truthy the body runs. If it's falsy on the very first check, the body runs **zero times**.

```python
i = 0
while i < 3:
    print(i)     # 0, 1, 2
    i += 1
print("end:", i) # end: 3
```

### Counting iterations

Tracing loop counts is a classic exam task. Track the variable state at each check:

```python
n = 10
count = 0
while n > 1:
    n //= 2      # 10 -> 5 -> 2 -> 1
    count += 1
print(count)     # 3
```

## 2. Sentinel-controlled loops

A **sentinel** is a special value that signals "stop" when the number of iterations isn't known in advance:

```python
total = 0
value = int(input("Number (0 to stop): "))
while value != 0:          # 0 is the sentinel
    total += value
    value = int(input("Number (0 to stop): "))
print("Total:", total)
```

The same thing with `while True` and `break` avoids repeating the `input` line:

```python
total = 0
while True:
    value = int(input("Number (0 to stop): "))
    if value == 0:
        break
    total += value
print("Total:", total)
```

## 3. Infinite loops

A loop whose condition never becomes falsy runs forever:

```python
i = 0
while i < 5:
    print(i)       # i never changes, so this prints 0 forever
```

`while True:` is a **deliberate** infinite loop. It's fine as long as a `break` (or `return` or an exception) exits it. Exam questions often hide an infinite loop by changing the wrong variable or stepping past the stop value:

```python
i = 1
while i != 10:
    i += 2         # 1, 3, 5, 7, 9, 11, ... never equals 10, so it never stops
```

You stop a runaway program with Ctrl+C, which raises `KeyboardInterrupt`.

## 4. The walrus operator `:=` (assignment expression)

`name := expression` **assigns and returns** the value, so you can assign inside an expression. It's available since Python 3.8.

```python
while (line := input("> ")) != "quit":
    print("You typed:", line)
```

This replaces the "read before the loop, read again at the end of the body" pattern.

```python
data = [3, 8, 1, 9]
if (n := len(data)) > 3:
    print(f"list too long ({n} elements)")   # list too long (4 elements)
```

Rules:
- `:=` has the **lowest precedence** of all operators, so parenthesize it when comparing: `(x := f()) != 0`. Without the parentheses, `x := f() != 0` assigns the *bool* `f() != 0` to `x`.
- An unparenthesized `x := 5` at statement level is a `SyntaxError`. Use plain `=` there.
- The name it binds lives in the current scope, so it's still available after the loop.

```python
values = [5, 0, 7]
i = 0
while (v := values[i]) != 0:
    print(v)       # 5
    i += 1
print(v)           # 0
```

## 5. `while ... else` *(beyond the syllabus)*

A `while` loop can have an `else` block. It runs when the loop ends **because the condition became false**, and **not** when the loop exits with `break`. This is covered with `break` in lesson 2.2c.

---

## Exam traps
- A falsy condition at the start means zero iterations.
- Make sure the loop variable actually changes; otherwise you have an infinite loop.
- `!=` with a step that skips the target value never terminates.
- Without parentheses, `x := a != b` binds the comparison result.
- The variable keeps its final value after the loop.

## Key takeaways
- `while` checks its condition before every iteration.
- Sentinel loops are written as `while value != SENTINEL` or as `while True` plus `break`.
- `:=` lets you read and test in a single expression.
