numbers = [10, 20, 30, 40, 30, 40, 50]

# option 1
print(list(set(numbers)))

# option 2
unique_nums = []
for num in numbers:
    if num not in unique_nums:
        unique_nums.append(num)

print(unique_nums)

# option 3
unique_nums = set()
for num in numbers:
    unique_nums.add(num)

print(unique_nums)

# option 4
unique_nums = set()
unique_nums.update(numbers)
print(unique_nums)
