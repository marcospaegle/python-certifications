# 5.1a File Handling

**Objectives covered:** `5.1.1`
**Exam section:** 5 – File Handling and Module Imports (14%, 5 items)

### What the exam expects (official syllabus, paraphrased)
- [ ] **5.1.1** – Open text files in modes `r`, `w`, `a`
- [ ] **5.1.1** – Read; write; append
- [ ] **5.1.1** – `with` for safe file access
- [ ] **5.1.1** – Recognize common errors when opening or accessing files

---

## 1. Opening a file

```python
f = open(path, mode="r", encoding=None)
```

`open()` returns a **file object**. Text mode is the default, and in text mode you read and write `str`.

| Mode | Meaning | If the file exists | If it doesn't exist | Position |
|---|---|---|---|---|
| `"r"` | read (the **default**) | opens it | **`FileNotFoundError`** | start |
| `"w"` | write | **truncates** it (erases the content) | creates it | start |
| `"a"` | append | keeps the content | creates it | **end**: every write appends |

(`"x"` for exclusive creation, `"+"` for read and write, and `"b"` for binary also exist, but they're outside the syllabus.)

Pass `encoding="utf-8"` explicitly for portable text handling.

## 2. The `with` statement (context manager)

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")
# the file is closed automatically here, even if an exception occurred
```

Without `with` you must call `f.close()` yourself. If you forget, written data may not be flushed to disk. Prefer `with` in every case.

```python
f = open("notes.txt")
try:
    data = f.read()
finally:
    f.close()        # this is what `with` does for you
```

After the `with` block the file is closed. Reading from it then raises `ValueError: I/O operation on closed file.`

## 3. Writing

```python
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("line 1\n")          # write() does NOT add a newline
    f.write("line 2\n")
    count = f.write("abc")       # returns the number of characters written -> 3
    f.writelines(["x\n", "y\n"]) # writes each string; no newlines are added either
    print("via print", file=f)   # print() can target a file (adds a newline)
```

- `write()` accepts **only `str`** in text mode: `f.write(42)` raises `TypeError: write() argument must be str, not int`. Use `f.write(str(42))`.
- Opening with `"w"` erases the existing content **immediately**, even if you never write anything.

## 4. Appending

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("new entry\n")       # added after the existing content
```

Running this twice gives two lines. Doing the same with `"w"` would leave just one.

## 5. Reading

Suppose `data.txt` contains:

```text
alpha
beta
gamma
```

| Method | Returns |
|---|---|
| `f.read()` | the **whole** file as one string |
| `f.read(n)` | up to `n` characters |
| `f.readline()` | the next line, **including** its `\n`; `""` at end of file |
| `f.readlines()` | a list of all lines, each with its `\n` |
| `for line in f:` | iterates line by line, memory-efficiently (each line keeps its `\n`) |

```python
with open("data.txt", encoding="utf-8") as f:
    print(repr(f.read()))        # 'alpha\nbeta\ngamma\n'

with open("data.txt", encoding="utf-8") as f:
    print(repr(f.readline()))    # 'alpha\n'
    print(repr(f.readline()))    # 'beta\n'

with open("data.txt", encoding="utf-8") as f:
    print(f.readlines())         # ['alpha\n', 'beta\n', 'gamma\n']

with open("data.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())      # strip the "\n", or print adds a blank line
```

The file object keeps a **current position**. After `read()` you're at the end of the file, and a second `read()` returns `""`.

```python
with open("data.txt", encoding="utf-8") as f:
    first = f.read()
    second = f.read()
print(repr(second))              # ''
```

### Processing pattern

```python
total = 0
with open("numbers.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:                   # skip blank lines
            total += int(line)     # int() tolerates surrounding whitespace anyway
```

## 6. Common file errors

| Error | Cause |
|---|---|
| `FileNotFoundError` | opening a missing file with `"r"` (or a missing directory with any mode) |
| `PermissionError` | no permission, or the path is a directory on some systems |
| `IsADirectoryError` | the path is a directory |
| `io.UnsupportedOperation` | reading a file opened with `"w"`, or writing one opened with `"r"` |
| `ValueError: I/O operation on closed file.` | using a file after `close()` or after the `with` block |
| `TypeError` | `write()` with a non-str argument |

`FileNotFoundError`, `PermissionError` and `IsADirectoryError` are all subclasses of `OSError`.

```python
try:
    with open("missing.txt", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError as e:
    print("No such file:", e.filename)
```

---

## Exam traps
- The default mode is `"r"`, and `"r"` on a missing file raises `FileNotFoundError`.
- `"w"` erases existing content; `"a"` preserves it and writes at the end.
- `write()` doesn't add `"\n"`, and it only accepts `str`.
- `readline()` and `readlines()` keep the trailing `\n`.
- A second `read()` returns `""`.
- `with` closes the file automatically, and using the file afterwards gives a `ValueError`.

## Key takeaways
- Use `open(path, mode)` inside a `with` block every time.
- The three modes are `r` (read; the file must exist), `w` (truncate or create) and `a` (append or create).
- Read with `read`, `readline`, `readlines` or by iterating; write with `write`.
