# 3.5a Strings: Literals, Indexing, Slicing, Methods

**Objectives covered:** `3.5.1`, `3.5.2`
**Exam section:** 3 – Data Collections

### What the exam expects (official syllabus, paraphrased)
- [ ] **3.5.1** – Single, double and triple quotes; escape sequences; quotes and apostrophes inside literals; multiline strings
- [ ] **3.5.1** – Positive and negative indexes; slicing with start, stop and step
- [ ] **3.5.1** – Immutability; `len()`; `in` / `not in` for substrings
- [ ] **3.5.2** – `lower()` `upper()` `capitalize()` `title()` `swapcase()`
- [ ] **3.5.2** – `find()`, `split()`, `join()`
- [ ] **3.5.2** – `strip()` `lstrip()` `rstrip()`, `replace()`
- [ ] **3.5.2** – Methods return new strings

---

A `str` is an **immutable sequence of Unicode characters**. There's no separate char type: a single character is just a string of length 1.

## 1. String literals (3.5.1)

```python
s1 = 'single'
s2 = "double"
s3 = '''triple
single'''
s4 = """triple
double"""
```

- Single and double quotes are interchangeable.
- Triple-quoted strings can span lines, and their line breaks become `\n` characters.

### Quotes inside literals

```python
"It's fine"              # use the other quote type
'He said "hi"'
'It\'s escaped'          # or escape it
"""Both ' and " inside"""
```

### Escape sequences

| Escape | Meaning |
|---|---|
| `\n` | newline |
| `\t` | tab |
| `\\` | a single backslash |
| `\'`, `\"` | a quote |

```python
print("a\nb")        # a / b (two lines)
print("c:\\temp")    # c:\temp
print(len("a\nb"))   # 3   (\n is ONE character)
print(len("\\"))     # 1
```

A **raw string** `r"..."` treats backslashes literally: `r"c:\new"` contains a backslash followed by `n`.

Multiline string vs `\n`:

```python
text = """line1
line2"""
print(text == "line1\nline2")   # True
```

## 2. Indexing, slicing, immutability, `len`, `in`

Strings index and slice exactly like lists:

```python
s = "Python"
s[0]       # 'P'
s[-1]      # 'n'
s[1:4]     # 'yth'
s[:2]      # 'Py'
s[::-1]    # 'nohtyP'
s[::2]     # 'Pto'
s[10]      # IndexError: string index out of range
s[2:100]   # 'thon'  (slices clip)
len(s)     # 6
len("")    # 0
```

### Immutability

```python
s = "hello"
s[0] = "H"        # TypeError: 'str' object does not support item assignment
s = "H" + s[1:]   # create a new string instead -> 'Hello'
```

### Substring membership

`in` on strings checks for **substrings**, not just single characters:

```python
"ell" in "hello"     # True
"" in "hello"        # True  (the empty string is in every string)
"H" in "hello"       # False (case-sensitive)
"x" not in "hello"   # True
```

### Iteration and comparison

```python
for ch in "abc": ...
"apple" < "banana"     # True  (lexicographic, by code point)
"a" < "B"              # False ('B' is 66 and 'a' is 97)
ord("a"), chr(97)      # (97, 'a')
```

## 3. String methods (3.5.2)

**All string methods return a NEW string** (or another value). The original is never modified.

```python
s = "hello"
s.upper()       # returns 'HELLO'
print(s)        # hello   (unchanged)
s = s.upper()   # rebind to keep the result
```

### Case methods

```python
"hello World".lower()       # 'hello world'
"hello World".upper()       # 'HELLO WORLD'
"hello WORLD".capitalize()  # 'Hello world'  first char upper, ALL the rest lower
"hello world".title()       # 'Hello World'  first letter of each word upper
"it's ok".title()           # "It'S Ok"      (title treats ' as a word break)
"Hello World".swapcase()    # 'hELLO wORLD'
```

### `find()`

`s.find(sub[, start[, end]])` returns the **lowest index** of `sub`, or **`-1`** if it isn't found:

```python
"banana".find("an")       # 1
"banana".find("an", 2)    # 3     (start searching at index 2)
"banana".find("x")        # -1
"banana".find("")         # 0
```

`index()` is like `find()` but raises `ValueError` when `sub` is missing. `count(sub)` counts non-overlapping occurrences.

### `split()`

```python
"a b  c".split()          # ['a', 'b', 'c']        no argument: split on any whitespace run, dropping empties
"a,b,,c".split(",")       # ['a', 'b', '', 'c']    explicit separator: empties are kept
"a b c".split(" ", 1)     # ['a', 'b c']           maxsplit
"abc".split(",")          # ['abc']
"".split()                # []
```

### `join()`

`sep.join(iterable_of_strings)`: the **separator is the object** the method is called on.

```python
", ".join(["a", "b", "c"])    # 'a, b, c'
"".join(["x", "y"])           # 'xy'
"-".join("abc")               # 'a-b-c'
", ".join([1, 2])             # TypeError: sequence item 0: expected str instance, int found
```

### `strip()`, `lstrip()`, `rstrip()`

With no argument these remove **whitespace** (spaces, `\t`, `\n`) from both ends, the left, or the right. With an argument they remove **any combination of the given characters**. The argument isn't a prefix or suffix:

```python
"  hi  ".strip()          # 'hi'
"  hi  ".lstrip()         # 'hi  '
"  hi  ".rstrip()         # '  hi'
"xxhixx".strip("x")       # 'hi'
"www.example.com".strip("wcom.")   # 'example'
"abcba".strip("ab")       # 'c'
```

### `replace()`

`s.replace(old, new[, count])` replaces **all** occurrences, or the first `count`:

```python
"banana".replace("a", "o")       # 'bonono'
"banana".replace("a", "o", 2)    # 'bonona'
"banana".replace("x", "y")       # 'banana'  (no error)
"aaa".replace("a", "")           # ''
```

### Chaining

Each method returns a string, so calls chain left to right:

```python
"  Hello World  ".strip().lower().replace("world", "py")   # 'hello py'
```

### Other useful methods

`startswith()`, `endswith()`, `isdigit()`, `isalpha()`, `isalnum()`, `isspace()`, `islower()` and `isupper()` all return bools:

```python
"123".isdigit()     # True
"12.5".isdigit()    # False
```

---

## Exam traps
- Strings are immutable: `s[0] = "x"` is a `TypeError`, and methods return new strings, so `s.upper()` alone changes nothing.
- `find` returns `-1`, while `index` raises `ValueError`.
- `split()` with no argument collapses whitespace runs; `split(" ")` doesn't.
- `join` is called on the separator, and every item must be a str.
- `strip("ab")` strips any of those characters, in any order.
- `capitalize()` lowercases the rest of the string.
- `len("\n")` is `1`.
- `"" in s` is always `True`.

## Key takeaways
- A string is an immutable, indexable and sliceable sequence of characters.
- Every method returns a new value, so rebind the name to keep it.
- Know the exact edge behaviour of `find`, `split`, `join`, `strip` and `replace`.
