# Think of an array like a row of numbered lockers — each locker holds one value and has a fixed position (index) starting from 0.

# Creating and using arrays (lists in Python)
fruits = ["apple", "banana", "mango"]

# Access by index (starts at 0)
print(fruits[0])   # apple
print(fruits[-1])  # mango (last item)

# Loop through
for fruit in fruits:
    print(fruit)

# Common operations
fruits.append("grape")   # add to end
fruits.pop()             # remove last
print(len(fruits))       # length = 3
