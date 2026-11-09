"""1.1.1 - Execution model: runtime errors stop execution at the failing line.

Run: python3 01_execution.py
"""

print("start")                     # -> start

# A runtime error is raised only when execution reaches it.
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("runtime error:", e)     # -> runtime error: division by zero

# A syntax error is found before any code runs. compile() lets us
# trigger one here without breaking this file.
try:
    compile('print("hello)', "<demo>", "exec")
except SyntaxError as e:
    print(type(e).__name__)        # -> SyntaxError

try:
    compile("if True:\nprint('x')", "<demo>", "exec")
except SyntaxError as e:
    print(type(e).__name__)        # -> IndentationError

print(issubclass(IndentationError, SyntaxError))  # -> True
