"""3.5.1 / 3.5.2 - Strings and string methods."""

print(len("a\nb"), len("\\"), len(r"c:\new"))  # -> 3 1 6
print("c:\\temp")                  # -> c:\temp
text = """line1
line2"""
print(text == "line1\nline2")      # -> True

s = "Python"
print(s[0], s[-1], s[1:4], s[:2])  # -> P n yth Py
print(s[::-1], s[::2], s[2:100])   # -> nohtyP Pto thon

try:
    s[0] = "J"
except TypeError as e:
    print(e)                       # -> 'str' object does not support item assignment

print("ell" in "hello", "" in "hello", "H" in "hello")  # -> True True False
print("a" < "B", ord("a"), chr(97))  # -> False 97 a

s = "hello"
s.upper()
print(s)                           # -> hello
print("hello WORLD".capitalize())  # -> Hello world
print("hello world".title(), "|", "it's ok".title())  # -> Hello World | It'S Ok
print("Hello World".swapcase())    # -> hELLO wORLD

print("banana".find("an"), "banana".find("an", 2), "banana".find("x"))  # -> 1 3 -1
print("banana".count("a"))         # -> 3

print("a b  c".split())            # -> ['a', 'b', 'c']
print("a b  c".split(" "))         # -> ['a', 'b', '', 'c']
print("a,b,,c".split(","))         # -> ['a', 'b', '', 'c']
print("a b c".split(" ", 1), "".split())  # -> ['a', 'b c'] []

print(", ".join(["a", "b", "c"]), "-".join("abc"))  # -> a, b, c a-b-c

print(repr("  hi  ".strip()), repr("  hi  ".lstrip()), repr("  hi  ".rstrip()))  # -> 'hi' 'hi  ' '  hi'
print("www.example.com".strip("wcom."), "abcba".strip("ab"))  # -> example c

print("banana".replace("a", "o"), "banana".replace("a", "o", 2))  # -> bonono bonona
print("  Hello World  ".strip().lower().replace("world", "py"))  # -> hello py
print("123".isdigit(), "12.5".isdigit(), "abc".isalpha())  # -> True False True
