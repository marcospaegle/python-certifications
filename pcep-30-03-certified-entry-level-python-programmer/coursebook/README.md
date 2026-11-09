# PCEP-30-03 Coursebook

A study book for **PCEP™ – Certified Entry-Level Python Programmer (PCEP-30-03)**, blueprint v1.5. It covers every one of the 35 exam objectives and nothing beyond them.

It's written for a reader who already knows how to program and is learning Python. Concepts are explained in terms of Python's own semantics, with the edge cases that exam questions are built on.

Exam facts (see [`../PCEP-30-03.md`](../PCEP-30-03.md) for full details): **35 questions, 50 minutes, 70% to pass**, with single-select, multiple-select, interactive and scenario-based items.

---

## How to use this book

1. Read the chapters in order. Later chapters build on the earlier ones.
2. Every lesson has the same structure: **Objectives covered → What the exam expects (the official syllabus checklist) → Concepts → Code with exact output → Exam traps → Key takeaways**. Tick off the checklist once you can do each item without notes.
3. The official profile of a passing candidate says they can **read, trace, complete and write** simple Python programs. Many objectives start with "Trace…" or "Recognize…", so practise predicting the exact output of every code block before reading the answer.
4. Sections marked ***(beyond the syllabus)*** cover constructs that the 30-03 syllabus doesn't list, such as loop `else`, `try`/`else`/`finally`, set operators and recursion. They're there so that exam code which happens to use them doesn't catch you out. Read them last.
5. Each chapter has an `examples/` folder with runnable scripts that mirror its lessons. In every script, each `print` is annotated with its expected output (`# -> ...`). Run them and change them:

   ```bash
   cd coursebook/01-python-fundamentals/examples
   python3 04_operators.py
   ```

6. Before the exam, re-read the **Exam traps** section of every lesson.

The book targets **Python 3.12+**.

---

## Contents

### Chapter 1 – Computer Programming and Python Fundamentals · 17% · 6 items
| Lesson | Objectives |
|---|---|
| [1.1 Language structure and code execution](01-python-fundamentals/01-language-and-execution.md) | 1.1.1 |
| [1.2 Program logic and structure](01-python-fundamentals/02-program-structure.md) | 1.2.1 |
| [1.3 Literals and variables](01-python-fundamentals/03-literals-and-variables.md) | 1.3.1, 1.3.2 |
| [1.4a Operators and expressions](01-python-fundamentals/04-operators-and-expressions.md) | 1.4.1 |
| [1.4b Console I/O and type conversion](01-python-fundamentals/05-console-io-and-conversion.md) | 1.4.2 |

### Chapter 2 – Control Flow: Conditional Blocks and Loops · 23% · 8 items
| Lesson | Objectives |
|---|---|
| [2.1 Conditional execution](02-control-flow/01-conditionals.md) | 2.1.1, 2.1.2, 2.1.3 |
| [2.2a `while` loops and the walrus operator](02-control-flow/02-while-and-walrus.md) | 2.2.1 |
| [2.2b `for` loops and `range()`](02-control-flow/03-for-and-range.md) | 2.2.2, 2.2.3 |
| [2.2c Nested loops, `break`, `continue`, `pass`](02-control-flow/04-nested-loops-and-loop-control.md) | 2.2.4, 2.2.5 |

### Chapter 3 – Data Collections: Lists, Tuples, Sets, Dictionaries, Strings · 26% · 9 items
| Lesson | Objectives |
|---|---|
| [3.1 Lists](03-data-collections/01-lists.md) | 3.1.1, 3.1.2, 3.1.3 |
| [3.2 Tuples](03-data-collections/02-tuples.md) | 3.2.1 |
| [3.3 Sets](03-data-collections/03-sets.md) | 3.3.1 |
| [3.4 Dictionaries](03-data-collections/04-dictionaries.md) | 3.4.1 |
| [3.5a Strings: literals, indexing, methods](03-data-collections/05-strings.md) | 3.5.1, 3.5.2 |
| [3.5b String formatting](03-data-collections/06-string-formatting.md) | 3.5.3 |

### Chapter 4 – Functions and Exceptions · 20% · 7 items
| Lesson | Objectives |
|---|---|
| [4.1a Defining and calling functions; `return`](04-functions-and-exceptions/01-defining-and-calling.md) | 4.1.1, 4.1.2 |
| [4.1b Parameters and arguments](04-functions-and-exceptions/02-parameters-and-arguments.md) | 4.1.3, 4.1.4 |
| [4.1c Scope](04-functions-and-exceptions/03-scope.md) | 4.1.5 |
| [4.2 Exceptions](04-functions-and-exceptions/04-exceptions.md) | 4.2.1, 4.2.2 |

### Chapter 5 – File Handling and Module Imports · 14% · 5 items
| Lesson | Objectives |
|---|---|
| [5.1a File handling](05-files-and-modules/01-file-handling.md) | 5.1.1 |
| [5.1b CSV files](05-files-and-modules/02-csv.md) | 5.1.2 |
| [5.2 Imports, `math` and `random`](05-files-and-modules/03-imports-math-random.md) | 5.2.1, 5.2.2, 5.2.3 |

---

## Objective → lesson map

| Objective | Topic | Lesson |
|---|---|---|
| 1.1.1 | Language structure, errors, interpreter vs compiler, execution | 1.1 |
| 1.2.1 | Keywords, expressions vs statements, indentation, comments | 1.2 |
| 1.3.1 | int/float/str/bool literals, float precision | 1.3 |
| 1.3.2 | Variables, references, naming rules, PEP 8 | 1.3 |
| 1.4.1 | Arithmetic/string/assignment/logical/relational operators, precedence | 1.4a |
| 1.4.2 | `print`, `input`, `int`/`float`/`str` | 1.4b |
| 2.1.1 | `if`, `if-else` | 2.1 |
| 2.1.2 | `if-elif-else` | 2.1 |
| 2.1.3 | Compound and nested conditions | 2.1 |
| 2.2.1 | `while`, sentinels, infinite loops, `:=` | 2.2a |
| 2.2.2 | `for … in` over iterables | 2.2b |
| 2.2.3 | `range()` | 2.2b |
| 2.2.4 | Nested loops | 2.2c |
| 2.2.5 | `break`, `continue`, `pass` | 2.2c |
| 3.1.1 | List creation, indexing, slicing, copying | 3.1 |
| 3.1.2 | List methods, `del`, sorting, `in`, `len` | 3.1 |
| 3.1.3 | 2D/3D lists | 3.1 |
| 3.2.1 | Tuples | 3.2 |
| 3.3.1 | Sets | 3.3 |
| 3.4.1 | Dictionaries | 3.4 |
| 3.5.1 | String literals, escapes, indexing, slicing, immutability | 3.5a |
| 3.5.2 | String methods | 3.5a |
| 3.5.3 | f-strings, `format()`, `%` | 3.5b |
| 4.1.1 | `def`, invocation, execution order | 4.1a |
| 4.1.2 | `return`, `None` | 4.1a |
| 4.1.3 | Parameters, positional/keyword args, defaults | 4.1b |
| 4.1.4 | `*args`, `**kwargs` | 4.1b |
| 4.1.5 | Scope, shadowing, `global` | 4.1c |
| 4.2.1 | Exception purpose and the core built-in exceptions | 4.2 |
| 4.2.2 | `try`/`except` | 4.2 |
| 5.1.1 | File modes, `with`, read/write/append, errors | 5.1a |
| 5.1.2 | `csv.reader`, `csv.writer` | 5.1b |
| 5.2.1 | `import` | 5.2 |
| 5.2.2 | `math`: `ceil`, `floor`, `trunc`, `sqrt` | 5.2 |
| 5.2.3 | `random`: `random`, `seed`, `choice`, `sample` | 5.2 |
