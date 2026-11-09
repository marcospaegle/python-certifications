"""3.1.1-3.1.3 - Lists."""

nums = [10, 20, 30, 40, 50]
print(nums[0], nums[-1], nums[-2])  # -> 10 50 40
print(nums[1:3], nums[:2], nums[2:])  # -> [20, 30] [10, 20] [30, 40, 50]
print(nums[-2:], nums[:-1])        # -> [40, 50] [10, 20, 30, 40]
print(nums[::2], nums[::-1])       # -> [10, 30, 50] [50, 40, 30, 20, 10]
print(nums[3:1], nums[3:1:-1])     # -> [] [40, 30]
print(nums[1:100], nums[-100:2])   # -> [20, 30, 40, 50] [10, 20]

try:
    nums[5]
except IndexError as e:
    print(e)                       # -> list index out of range

# Alias vs copy
a = [1, 2, 3]
alias = a
copy1 = a[:]
a.append(4)
print(alias, copy1)                # -> [1, 2, 3, 4] [1, 2, 3]

grid = [[1, 2], [3, 4]]
g2 = grid[:]
g2[0][0] = 99
print(grid)                        # -> [[99, 2], [3, 4]]

nums = [1, 2, 3, 4, 5]
nums[1:3] = ["a", "b", "c"]
print(nums)                        # -> [1, 'a', 'b', 'c', 4, 5]

# Methods
nums = [3, 1, 2]
nums.append([4, 5])
print(nums)                        # -> [3, 1, 2, [4, 5]]
nums = [3, 1, 2]
nums.extend([4, 5])
print(nums)                        # -> [3, 1, 2, 4, 5]

nums = [10, 20, 30]
nums.insert(1, 15)
nums.insert(100, 99)
nums.insert(-1, 0)
print(nums)                        # -> [10, 15, 20, 30, 0, 99]
print(nums.index(20))              # -> 2
nums.remove(0)
print(nums.pop(), nums)            # -> 99 [10, 15, 20, 30]
del nums[0]
print(nums)                        # -> [15, 20, 30]

data = [3, 1, 2]
result = data.sort()
print(result, data)                # -> None [1, 2, 3]
data = [3, 1, 2]
print(sorted(data), data)          # -> [1, 2, 3] [3, 1, 2]
print(sorted(data, reverse=True))  # -> [3, 2, 1]
print(sorted(["banana", "Apple", "cherry"]))  # -> ['Apple', 'banana', 'cherry']
print(sorted("cba"))               # -> ['a', 'b', 'c']
print(sum([1, 2, 3]), max([4, 9, 2]), min([4, 9, 2]))  # -> 6 9 2
print(2 in data, 7 not in data, len(data))  # -> True True 3

# Modifying while iterating skips items
nums = [1, 2, 2, 3]
for n in nums:
    if n == 2:
        nums.remove(n)
print(nums)                        # -> [1, 2, 3]

# 2D / 3D
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1], matrix[1][2], matrix[-1][-1])  # -> [4, 5, 6] 6 9
col = []
for row in matrix:
    col.append(row[1])
print(col)                         # -> [2, 5, 8]
cube = [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
print(cube[1][0][1])               # -> 5

bad = [[0] * 3] * 2
bad[0][0] = 1
print(bad)                         # -> [[1, 0, 0], [1, 0, 0]]
good = []
for _ in range(2):
    good.append([0] * 3)
good[0][0] = 1
print(good)                        # -> [[1, 0, 0], [0, 0, 0]]
