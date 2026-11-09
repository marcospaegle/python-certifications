# 1.2 Program Logic and Structure

**Objectives covered:** `1.2.1`
**Exam section:** 1 – Computer Programming and Python Fundamentals

### What the exam expects (official syllabus, paraphrased)
- Recognize keywords and why they can't be identifiers
- Distinguish expressions, statements and keywords
- Use indentation to define blocks
- Recognize errors caused by incorrect or inconsistent indentation
- Use comments to document code and to temporarily disable lines

---

## 1. Keywords

Keywords are reserved words. They **cannot be used as identifiers** (variable, function or parameter names). Python 3.12 has 35 of them:

```text
False   None    True    and     as      assert  async   await
break   class   continue def    del     elif    else    except
finally for     from    global  if      import  in      is
lambda  nonlocal not    or      pass    raise   return  try
while   with    yield
```

```python
import keyword
print(keyword.kwlist)        # the full list
print(keyword.iskeyword("if"))   # True
```

```python
class = 5    # SyntaxError: invalid syntax
True = 1     # SyntaxError: cannot assign to True
```

Important nuances:
- Only `True`, `False` and `None` are capitalized. `true` is a perfectly legal identifier, and an undefined one (`NameError`).
- **Built-in function names are NOT keywords.** `print`, `input`, `len`, `list`, `str`, `int`, `sum` and `max` can be reassigned. That's legal but destructive:

```python
print = 5
print("hi")       # TypeError: 'int' object is not callable
```

- **Soft keywords** (`match`, `case`, `_`, `type`) are only reserved in specific contexts. `match = 3` is legal.

## 2. Expressions vs statements

- An **expression** is anything that evaluates to a value: `2 + 3`, `x`, `len(s)`, `a > b`, `"x" * 3`, a function call.
- A **statement** is a unit of execution that does something: an assignment `x = 5`, `if`, `while`, `for`, `def`, `return`, `import`, `pass`, `del`.
- An **expression statement** is an expression used on its own as a statement. A function call such as `print("hi")` is the typical case.

Assignment (`=`) is a **statement**, not an expression, so it cannot appear inside an `if` condition:

```python
if x = 5:         # SyntaxError
    ...
```

The walrus operator `:=` exists precisely to allow assignment *inside* an expression (covered in Chapter 2).

**Keywords vs statements:** many statements begin with a keyword (`if`, `while`, `return`), but some keywords are operators that build expressions: `and`, `or`, `not`, `in`, `is`, `lambda`, plus the values `True`, `False` and `None`.

## 3. Indentation and code blocks

Python delimits blocks **by indentation**, not braces. A compound statement header ends with a colon `:` and its body must be indented more deeply than the header:

```python
if temperature > 30:
    print("hot")          # inside the if block
    print("drink water")  # still inside
print("done")             # back at the outer level, always runs
```

Rules:
- PEP 8 recommends **4 spaces** per level. The amount is up to you, but it must be **consistent within a block**.
- Mixing tabs and spaces in a way that makes indentation ambiguous raises `TabError` (a subclass of `IndentationError`).
- A block can't be empty. Use `pass` as a placeholder.
- A simple statement may follow the colon on the same line (`if x: print(x)`). That's legal but discouraged.

Indentation errors:

```python
print("a")
    print("b")        # IndentationError: unexpected indent

if True:
print("x")            # IndentationError: expected an indented block after 'if' statement on line 1

if True:
        print("a")
    print("b")        # IndentationError: unindent does not match any outer indentation level
```

### Line structure
- One statement per line is the norm. `;` can separate statements on one line (`a = 1; b = 2`), but it's discouraged.
- **Implicit line joining:** inside `()`, `[]` or `{}` an expression can span multiple lines freely.
- **Explicit line joining:** a backslash `\` at the end of a line continues it.

```python
total = (1 +
         2 +
         3)
total = 1 + \
        2
```

## 4. Comments

- `#` starts a comment that runs to the end of the line. The interpreter ignores it.
- A `#` **inside a string literal** isn't a comment: `print("#1")` prints `#1`.
- Python has no multi-line comment syntax. Use a `#` on each line. A bare triple-quoted string (`"""..."""`) is technically a string expression statement, not a comment. When it's the first statement in a module or function it becomes a **docstring**.

```python
# This whole line is a comment
x = 10  # inline comment
```

Comments have two uses:
- **Documenting code:** explain *why* something is done. Don't restate what the code obviously does.
- **Temporarily disabling code ("commenting out"):** put a `#` in front of a line so it doesn't run, without deleting it.

```python
print("step 1")
# print("step 2")   # disabled: this line no longer runs
print("step 3")
# output: step 1 / step 3
```

When you comment out lines, the remaining code must still be valid. Commenting out the only line of a block leaves the block empty, which is an `IndentationError`:

```python
if True:
    # print("x")
print("after")      # IndentationError: expected an indented block after 'if' statement
```

---

## Exam traps
- `print`, `len`, `list` and `str` aren't keywords: assigning to them is legal and breaks later calls.
- `True`, `False` and `None` are keywords (capitalized); `true` is not.
- `=` inside an `if` condition is a `SyntaxError`.
- Code at a lower indentation level after a block **always runs**, because it isn't part of the block.
- Indentation errors are syntax errors, so nothing in the file runs.
- A `#` inside quotes isn't a comment.

## Key takeaways
- There are 35 keywords, and they're reserved.
- Expressions produce values; statements perform actions.
- A `:` plus deeper indentation makes a block; `pass` fills an empty block.
- `#` comments run to the end of the line.
