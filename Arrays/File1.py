'''In Python, arrays are not a built-in data type like in some other programming languages. Instead, Python provides
a powerful and flexible built-in data structure called a list, which can be used to implement arrays. Lists in Python
can hold elements of different data types and are dynamic, meaning they can grow or shrink in size as needed.'''

my_lst = list()
my_lst.append(1)
my_lst.append(2)
my_lst.append(3)
my_lst.append(4)
my_lst.append(5)
my_lst.append(6)

# Accessing Elements

first_element = my_lst[0]
second_element = my_lst[1]

# Slicing

subset = my_lst[1:3]  # doesnt include last one!
print(subset)

# Reversing

reversed_list = my_lst[::-1]
print(reversed_list)

# Selecting Every Nth Element

every_second = my_lst[::2]
print(every_second)

# Copying a list
lst_copy = my_lst[:]
print(id(my_lst))
print(id(lst_copy))

new_copy = my_lst.copy()
print(id(my_lst))
print(id(new_copy))

# Modifying elements using list comprehension
my_lst = [x ** 2 for x in my_lst]
print(my_lst)

# deleting elements
my_lst[0:2] = []
print(my_lst)
my_lst = [1, 4] + my_lst
print(my_lst)

# Get the last N elements
last_three = my_lst[-3:]
print(last_three)

# Checking for Palindromes
is_pal = my_lst == my_lst[::-1]
print(is_pal)

# Grouping into pairs or tuples
pairs = [(my_lst[i], my_lst[i + 1]) for i in range(0, len(my_lst), 2)]
print(pairs)

# Flattening a nested list
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested for item in sublist]  # sublist in nested, then item in sublist, pull item
print(flattened)

# adding and removing elements
flattened.append(10)  # append is for end
print(flattened)
flattened.insert(0, 0)  # insert is for position
print(flattened)

flattened.pop()  # removes from end
print(flattened)
flattened.pop(1)  # removes from position
print(flattened)
