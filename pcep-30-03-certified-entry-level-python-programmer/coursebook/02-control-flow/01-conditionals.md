# 2.1 Conditional Execution

**Objectives covered:** `2.1.1`, `2.1.2`, `2.1.3`
**Exam section:** 2 – Control Flow: Conditional Blocks and Loops (23%, 8 items)

### What the exam expects (official syllabus, paraphrased)
- `if` and `if-else`; conditions from Boolean expressions
- Trace which branch runs; recognize when a block is skipped
- `if-elif` and `if-elif-else` with a fallback
- Conditions are evaluated in order until one matches
- Trace multi-branch structures
- Recognize misordered, redundant or unreachable branches
- Multiple conditional statements in one program
- Nested conditionals
- Combined Boolean expressions in conditions
- Trace compound structures; identify unreachable, redundant or misordered branches

---

## 1. `if` and `if-else` (2.1.1)

```python
if condition:
    block_executed_when_truthy
else:
    block_executed_when_falsy
```

- The condition can be **any expression**. It's evaluated for truthiness (see 1.3), so it doesn't have to be a `bool`.
- Parentheses around the condition are optional and usually omitted: `if (x > 0):` is legal but unidiomatic.
- `else` is optional, and it has no condition.
- The colon after the condition and after `else` is mandatory.

```python
x = 0
if x:
    print("truthy")
else:
    print("falsy")       # printed: 0 is falsy

items = []
if not items:
    print("empty")       # idiomatic emptiness test
```

### Tracing skipped blocks

When the condition is false and there's no `else`, the whole block is skipped and execution continues after it:

```python
n = 5
if n > 10:
    print("big")
    n = 0
print(n)                 # 5  (the assignment inside the block never ran)
```

## 2. `if-elif-else` chains (2.1.2)

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"      # first true condition wins
elif score >= 70:
    grade = "C"
else:
    grade = "F"      # fallback: runs only if no condition was true
print(grade)         # B
```

Semantics:
- Conditions are tested **top to bottom**.
- **Only the first branch whose condition is true runs.** Later conditions aren't even evaluated.
- `else` (optional) runs only if every condition was false.
- An `if/elif/elif` chain without `else` may run **zero** branches.

### Misordered branches

Order matters when conditions overlap. Here the broad condition comes first, so the later branches are unreachable:

```python
score = 95
if score >= 70:
    grade = "C"      # 95 lands here
elif score >= 90:
    grade = "A"      # unreachable: anything >= 90 is also >= 70
print(grade)         # C
```

### Chain vs separate `if`s

Separate `if` statements are tested **independently**, so several can run:

```python
x = 15
if x > 5:
    print("> 5")
if x > 10:
    print("> 10")    # also printed
```

```python
x = 15
if x > 5:
    print("> 5")
elif x > 10:
    print("> 10")    # NOT printed: the chain stopped at the first match
```

## 3. Compound and nested conditionals (2.1.3)

### Compound conditions with `and`, `or`, `not`

```python
age, member = 25, True
if age >= 18 and member:
    print("access")
if age < 13 or age > 65:
    print("discount")
if not member:
    print("sign up")
```

Remember the precedence: `not` > `and` > `or`. So `a or b and c` means `a or (b and c)`. Short-circuiting applies, too (see 1.4.1).

Chained comparisons are often the cleanest range check: `if 0 <= x < 10:`.

### Nested conditionals

```python
x = 7
if x > 0:
    if x % 2 == 0:
        print("positive even")
    else:
        print("positive odd")   # printed
else:
    print("non-positive")
```

An `else` belongs to the `if` at the **same indentation level**. Indentation removes any ambiguity about which `if` an `else` belongs to.

### Redundant and unreachable branches

```python
if x > 10:
    ...
elif x > 20:      # unreachable: x > 20 implies x > 10
    ...

if x > 0:
    ...
elif x <= 0:      # redundant: this could just be `else`
    ...

if x > 5 and x > 3:   # the `x > 3` part is redundant
    ...
```

### Conditional expression (ternary) *(beyond the syllabus)*

You'll meet it in exam code:

```python
label = "even" if n % 2 == 0 else "odd"
```

---

## Exam traps
- Only the **first** true branch of an `if/elif` chain runs. Separate `if`s can all run.
- Overlapping conditions in the wrong order make later branches unreachable.
- Conditions are truthiness tests: `if "0":` is true, and `if []:` is false.
- `else` pairs with the `if` at the same indentation.
- A statement after a skipped block always runs.
- `if x = 5:` is a `SyntaxError`.

## Key takeaways
- `if`, `elif` and `else` are evaluated top to bottom, and at most one branch runs.
- `not`, `and` and `or` build compound conditions, with short-circuiting.
- Look out for overlapping or misordered conditions.
