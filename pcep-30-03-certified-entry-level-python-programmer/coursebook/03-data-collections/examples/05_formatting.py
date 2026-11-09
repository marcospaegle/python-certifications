"""3.5.3 - f-strings, format(), % formatting."""

name, age = "Ada", 36
print(f"{name} is {age}")          # -> Ada is 36
print(f"{age + 1} next year")      # -> 37 next year
print(f"{2 * 3 = }")               # -> 2 * 3 = 6
print(f"{{literal braces}}")       # -> {literal braces}

print(f"{3.14159:.2f}", f"{2.5:.0f}", f"{9.999:.2f}")  # -> 3.14 2 10.00
print(f"[{'ab':5}]", f"[{42:5}]")  # -> [ab   ] [   42]
print(f"[{'ab':>5}]", f"[{'ab':*^6}]")  # -> [   ab] [**ab**]
print(f"{42:05}", f"{1234567:,}", f"{1234.5:,.2f}")  # -> 00042 1,234,567 1,234.50
print(f"{0.25:.1%}", f"{1234.5:.2e}")  # -> 25.0% 1.23e+03

print("{} and {}".format("a", "b"))  # -> a and b
print("{1} and {0}".format("a", "b"))  # -> b and a
print("{0}{0}{1}".format("x", "y"))  # -> xxy
print("{name} is {age}".format(name="Ada", age=36))  # -> Ada is 36
print("{:>6}|".format("hi"))       # ->     hi|

print("Hello, %s" % "Ada")         # -> Hello, Ada
print("%s is %d" % ("Ada", 36))    # -> Ada is 36
print("%f" % 3.14, "%.2f" % 3.14159, "%d" % 3.99)  # -> 3.140000 3.14 3
print("%5d|" % 42, "%-5d|" % 42, "%05d" % 42)  # ->    42| 42   | 00042
print("%d%%" % 50)                 # -> 50%

try:
    "%s and %s" % ("a",)
except TypeError as e:
    print(e)                       # -> not enough arguments for format string
