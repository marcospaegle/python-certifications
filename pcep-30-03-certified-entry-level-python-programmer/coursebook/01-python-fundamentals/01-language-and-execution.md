# 1.1 Language Structure and Code Execution

**Objectives covered:** `1.1.1`
**Exam section:** 1 – Computer Programming and Python Fundamentals (17%, 6 items)

### What the exam expects (official syllabus, paraphrased)
- Define lexis, syntax and semantics and their roles
- Distinguish lexical, syntactic and semantic errors
- Define interpretation and compilation; the roles of an interpreter and a compiler
- Compare interpreted and compiled execution models
- Explain how Python source code is processed and executed

---

## 1. Lexis, syntax, semantics

Every language is defined on three levels, and the exam expects you to tell them apart.

| Level | Defines | In Python |
|---|---|---|
| **Lexis** | The vocabulary: which tokens exist | Keywords (`if`, `def`), identifiers (`total`), literals (`42`, `"hi"`), operators (`//`), delimiters (`(`, `:`), plus **NEWLINE / INDENT / DEDENT** tokens |
| **Syntax** | How tokens combine into valid constructs | `if <expr>:` followed by an indented block, `def name(params):` |
| **Semantics** | What a syntactically valid program *means* | `"3" + 4` is valid syntax, but it means "add a str to an int", which is undefined, so it raises `TypeError` |

Python turns indentation into tokens. The tokenizer emits `INDENT` and `DEDENT` tokens, which is why indentation is **part of the grammar**, not just style.

## 2. The three kinds of errors

| Error kind | Detected when | Typical Python exception |
|---|---|---|
| **Lexical** | Tokenizing: a character sequence isn't a valid token | `SyntaxError` (e.g. unterminated string literal, invalid character `$`, `07` as a decimal literal) |
| **Syntactic** | Parsing: valid tokens in an invalid arrangement | `SyntaxError`, `IndentationError` (a subclass of `SyntaxError`) |
| **Semantic / runtime** | Execution: the code runs but an operation is invalid, or the logic is wrong | `TypeError`, `NameError`, `ZeroDivisionError`, … or simply wrong output with no error |

```python
print("hello)        # lexical:   SyntaxError: unterminated string literal
if x > 1 print(x)    # syntactic: SyntaxError: expected ':'
print(10 / 0)        # runtime:   ZeroDivisionError: division by zero
average = a + b / 2  # logical:   no error at all, wrong result (precedence)
```

**Key exam fact:** lexical and syntax errors are found **before any line runs**. If a file contains a `SyntaxError` on line 50, then line 1's `print()` never executes. Runtime errors, by contrast, are raised only when execution actually reaches the faulty line.

```python
print("start")
print(1 / 0)     # runtime error, so "start" IS printed first
```

```python
print("start")
print(1 +)       # syntax error, so NOTHING is printed
```

## 3. Compilation vs interpretation

| | Compiler | Interpreter |
|---|---|---|
| Translation | Whole program translated to machine code ahead of time | Source is read and executed on the fly |
| Output | A standalone executable | No separate executable; the interpreter must be present |
| Errors | Reported at compile time | Reported when encountered |
| Speed | Usually faster at run time | Usually slower, but quicker to iterate |

Python is conventionally classified as an **interpreted** language, and that's the answer the exam wants. In detail, the reference implementation (**CPython**, written in C) works like this:

1. **Tokenize** the source into tokens.
2. **Parse** them into an Abstract Syntax Tree (AST). Lexical and syntax errors are raised here.
3. **Compile** the AST into **bytecode**, an intermediate, platform-independent instruction set. Bytecode for imported modules is cached in `__pycache__/*.pyc`.
4. **Execute** the bytecode in the **Python Virtual Machine** (PVM), one instruction at a time. Runtime errors are raised here.

So CPython does compile internally, but only to bytecode for its own VM, not to native machine code. Other implementations exist (PyPy, Jython, MicroPython). CPython is the standard, and it's the one you get from python.org.

## 4. How a Python program is run

- A source file has a **`.py`** extension and is plain UTF-8 text.
- `python3 script.py` executes the file top to bottom. There's no mandatory `main` function: module-level statements simply run in order.
- `python3` with no arguments starts the **REPL** (Read–Eval–Print Loop), the interactive shell with the `>>>` prompt. In the REPL, the value of a bare expression is echoed automatically. In a script it isn't, so you need `print()`.

```text
>>> 2 + 3
5
```

In a script, a bare `2 + 3` line computes the value and silently discards it.

## 5. Python versions

- **Python 3** is the language of the exam. Python 2 is dead (end of life in 2020) and incompatible with it (for example, `print` was a statement there).
- This coursebook assumes **Python 3.12+**.

---

## Exam traps
- `IndentationError` **is a** `SyntaxError`, so it's detected before execution starts.
- A syntax error anywhere in the file means **no output at all**, even from earlier lines.
- A runtime error stops execution **at that line**. Earlier output has already happened.
- "Python is interpreted" is the expected classification, even though bytecode exists.
- The REPL echoes expression values; scripts don't.

## Key takeaways
- Lexis is the tokens, syntax is the structure, and semantics is the meaning.
- The pipeline is source → tokens → AST (Abstract Syntax Tree) → bytecode → PVM (Python Virtual Machine).
- Lexical and syntax errors happen before execution; runtime errors happen during it; logic errors produce no error at all.
