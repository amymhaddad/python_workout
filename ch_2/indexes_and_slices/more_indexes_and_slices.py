# Swap the first element of a list with the last, the second with the second-to-last, and so forth —
# so that the list [10, 20, 30, 40, 50] becomes [50, 40, 30, 20, 10].

list1 = [10, 20, 30, 40, 50]

# Option 1
list1.reverse()
print(list1)

# Option 2
list1[:] = list1[::-1]
print(list1)


# Given a list of integers mylist, produce a new list, in which even numbers in mylist are multiplied by 5 and odd numbers in mylist are multiplied by 3.
mylist = list(range(10))
new_list = []
for i, number in enumerate(mylist):
    if i == 0 or i % 2 == 0:
        new_list.append(number * 5)
    else:
        new_list.append(number * 3)

print(new_list)


# You can modify a list while iterating over it — something that is often a bad idea, but which can help in certain situations.
# Start with a three-element list of numbers, [10, 20, 30].
# Print each number, and then append 5x that number to the end of the list. So when you get to 10, add 50 to the end of the list.
# And when you get to 20, add 100 to the end of the list.
# Stop printing (and exit the loop) when 5x the current number would be greater than 1,000.

list = [10, 20, 30]

for i, number in enumerate(list):
    if number > 1000:
        break
    else:
        print(number)
        list.append(number * 5)
