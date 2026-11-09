"""2.2.4 / 2.2.5 - nested loops, break, continue, pass, loop else."""

pairs = []
for i in range(3):
    for j in range(2):
        pairs.append((i, j))
print(len(pairs), pairs[:3])       # -> 6 [(0, 0), (0, 1), (1, 0)]

for i in range(1, 4):
    print("*" * i)
# -> *
# -> **
# -> ***

count = 0
for i in range(4):
    for j in range(i):
        count += 1
print(count)                       # -> 6

for n in range(2, 10):
    is_prime = True
    for d in range(2, n):
        if n % d == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
print()                            # -> 2 3 5 7

# break leaves only the inner loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j, end=" | ")
print()                            # -> 0 0 | 1 0 | 2 0 |

# continue
for n in range(6):
    if n % 2 == 0:
        continue
    print(n, end=" ")
print()                            # -> 1 3 5

# pass does not skip
for i in range(2):
    pass
    print(i, end=" ")
print()                            # -> 0 1

# loop else
for n in [1, 3, 5]:
    if n % 2 == 0:
        print("found even")
        break
else:
    print("no even number")        # -> no even number

for n in [1, 4, 5]:
    if n % 2 == 0:
        print("found even", n)     # -> found even 4
        break
else:
    print("no even number")

for x in []:
    print(x)
else:
    print("else runs")             # -> else runs
