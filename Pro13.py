#Use of map(), filter(), reduce()

from functools import reduce

nums = [1, 2, 3, 4, 5]

# map() 
squares = list(map(lambda x: x*x, nums))
print("Squares:", squares)

# filter() 
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)

# reduce()
total = reduce(lambda a, b: a + b, nums)
print("Total:", total)
