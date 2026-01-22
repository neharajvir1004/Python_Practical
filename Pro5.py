#Largest Odd Number

largest_odd = 0

print("Enter 10 numbers:")

for i in range(10):
    n = int(input("Enter number: "))

    if n % 2 != 0:        
        if n > largest_odd:
            largest_odd = n

if largest_odd != 0:
    print("Largest odd number is:", largest_odd)
else:
    print("No odd number entered")
