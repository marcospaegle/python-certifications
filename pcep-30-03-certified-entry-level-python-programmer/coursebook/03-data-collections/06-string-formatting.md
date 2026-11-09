# 3.5b String Formatting

**Objectives covered:** `3.5.3`
**Exam section:** 3 – Data Collections

### What the exam expects (official syllabus, paraphrased)
- [ ] **3.5.3** – Construct f-strings, with variables and expressions in `{}`
- [ ] **3.5.3** – **Recognize** basic `format()` formatting
- [ ] **3.5.3** – **Recognize** basic legacy `%` formatting

Python has three formatting mechanisms. All three are tested.

---

## 1. f-strings (formatted string literals)

Prefix the literal with `f` (or `F`). Expressions inside `{}` are evaluated **at runtime** and inserted:

```python
name, age = "Ada", 36
print(f"{name} is {age}")            # Ada is 36
print(f"{age + 1} next year")        # 37 next year
print(f"{name.upper()}")             # ADA
print(f"{2 * 3 = }")                 # 2 * 3 = 6   (the "=" debug specifier)
print(f"{{literal braces}}")         # {literal braces}
```

Since Python 3.12, an f-string can contain the **same quote type** inside its braces (`f"{d["key"]}"`). Before 3.12 you had to use the other quote type: `f"{d['key']}"`. The second form works everywhere, so prefer it.

## 2. Format specifiers: `{value:spec}`

The part after `:` is a format spec, shared by f-strings and `format()`:

`[fill][align][width][,][.precision][type]`

| Spec | Meaning | Example | Result |
|---|---|---|---|
| `.2f` | fixed-point, 2 decimals (rounded) | `f"{3.14159:.2f}"` | `3.14` |
| `.0f` | no decimals | `f"{2.5:.0f}"` | `2` (round-half-even) |
| `10` | minimum width 10 | `f"{'ab':10}"` | `'ab        '` |
| `<` `>` `^` | left, right, center alignment | `f"{'ab':>5}"` | `'   ab'` |
| fill char | before the alignment | `f"{'ab':*^6}"` | `'**ab**'` |
| `05` | zero-pad to width 5 | `f"{42:05}"` | `00042` |
| `,` | thousands separator | `f"{1234567:,}"` | `1,234,567` |
| `d` | integer | `f"{42:d}"` | `42` |
| `%` | percentage | `f"{0.25:.1%}"` | `25.0%` |
| `e` | scientific | `f"{1234.5:.2e}"` | `1.23e+03` |

Defaults: **strings align left, numbers align right**.

```python
print(f"[{'ab':5}]")     # [ab   ]
print(f"[{42:5}]")       # [   42]
print(f"{9.999:.2f}")    # 10.00
print(f"{1234.5:,.2f}")  # 1,234.50
```

## 3. `str.format()`

Placeholders `{}` are filled from the arguments to `.format()`:

```python
"{} and {}".format("a", "b")            # 'a and b'       positional, in order
"{1} and {0}".format("a", "b")          # 'b and a'       explicit indexes
"{0}{0}{1}".format("x", "y")            # 'xxy'           reuse
"{name} is {age}".format(name="Ada", age=36)   # keyword
"{:.2f}".format(3.14159)                # '3.14'          same format spec
"{:>6}|".format("hi")                   # '    hi|'
"{} {}".format("only one")              # IndexError: Replacement index 1 out of range for positional args tuple
```

You can't mix automatic `{}` and manual `{0}` numbering in one string (`ValueError`).

## 4. Legacy `%` formatting (printf-style)

`format_string % values`. A single value can be given alone; several values must be a **tuple**:

| Conversion | Meaning |
|---|---|
| `%s` | str() of the value |
| `%d` (or `%i`) | integer (a float is truncated) |
| `%f` | float, 6 decimals by default |
| `%.2f` | float, 2 decimals |
| `%5d`, `%-5d` | width 5, right- or left-aligned |
| `%05d` | zero-padded |
| `%%` | a literal `%` |

```python
"Hello, %s" % "Ada"                 # 'Hello, Ada'
"%s is %d" % ("Ada", 36)            # 'Ada is 36'
"%f" % 3.14                         # '3.140000'
"%.2f" % 3.14159                    # '3.14'
"%d" % 3.99                         # '3'   (truncated)
"%5d|" % 42                         # '   42|'
"%-5d|" % 42                        # '42   |'
"%05d" % 42                         # '00042'
"%d%%" % 50                         # '50%'
"%s and %s" % ("a",)                # TypeError: not enough arguments for format string
"%d" % "5"                          # TypeError: %d format: a real number is required, not str
```

## 5. Comparing the three

```python
pi = 3.14159
f"{pi:.2f}"            # '3.14'
"{:.2f}".format(pi)    # '3.14'
"%.2f" % pi            # '3.14'
```

Prefer f-strings in modern code. Recognize the other two, because exam questions use all three.

---

## Exam traps
- `.2f` rounds, it doesn't truncate: `f"{9.999:.2f}"` gives `10.00`.
- `%d` truncates a float.
- Strings align left and numbers right by default.
- `{{` and `}}` produce literal braces.
- `"{1}{0}".format("a", "b")` gives `ba`.
- With several values, `%` needs a tuple.
- `%%` produces a literal percent sign.

## Key takeaways
- f-strings evaluate their expressions inline, and they're the default choice.
- `format()` uses `{}` placeholders filled positionally or by keyword.
- `%` is the legacy printf style: `%s`, `%d`, `%f`, `%.nf`, `%%`.
- The format spec (`fill`, `align`, `width`, `,`, `.precision`, `type`) is shared by f-strings and `format()`.
