"""2.1.1-2.1.3 - Conditional execution."""

x = 0
if x:
    print("truthy")
else:
    print("falsy")                 # -> falsy

n = 5
if n > 10:
    n = 0
print(n)                           # -> 5

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(grade)                       # -> B

# Misordered branches: "A" is unreachable
score = 95
if score >= 70:
    grade = "C"
elif score >= 90:
    grade = "A"
print(grade)                       # -> C

# Separate ifs vs elif chain
x = 15
if x > 5:
    print("> 5")                   # -> > 5
if x > 10:
    print("> 10")                  # -> > 10
if x > 5:
    print("chain > 5")             # -> chain > 5
elif x > 10:
    print("chain > 10")

# Nested
x = 7
if x > 0:
    if x % 2 == 0:
        print("positive even")
    else:
        print("positive odd")      # -> positive odd
else:
    print("non-positive")

# Compound + precedence (not > and > or)
a, b, c = True, False, False
print(a or b and c)                # -> True
print((a or b) and c)              # -> False

# Conditional expression
n = 4
print("even" if n % 2 == 0 else "odd")  # -> even
