"""2.2.1 - while loops, sentinels, walrus operator."""

i = 0
while i < 3:
    print(i, end=" ")
    i += 1
print()                            # -> 0 1 2
print("end:", i)                   # -> end: 3

n = 10
count = 0
while n > 1:
    n //= 2
    count += 1
print(count)                       # -> 3

# Sentinel loop over a fixed list (instead of input) so it runs unattended
values = [5, 3, 0, 9]
total = 0
idx = 0
while values[idx] != 0:
    total += values[idx]
    idx += 1
print("Total:", total)             # -> Total: 8

# Walrus in a while condition
values = [5, 7, 0, 2]
i = 0
while (v := values[i]) != 0:
    i += 1
print(v, i)                        # -> 0 2

data = [3, 8, 1, 9]
if (n := len(data)) > 3:
    print(f"list too long ({n} elements)")  # -> list too long (4 elements)

# Missing parentheses: x gets the bool
if x := len(data) > 3:
    print(x)                       # -> True

# while ... else
i = 0
while i < 3:
    i += 1
else:
    print("done", i)               # -> done 3
