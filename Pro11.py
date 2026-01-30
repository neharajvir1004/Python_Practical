#sum of arg.

def total_numbers(*nums):
    total = 0
    for n in nums:
        total += n
    print("Total =", total)


total_numbers(10, 20, 30)
total_numbers(5, 15, 25, 35)
