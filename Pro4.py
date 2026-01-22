#Armstrong numbers

print("Enter 10 numbers:")

for i in range(10):
    n = int(input("Enter number: "))
    temp = n
    sum = 0

    while temp > 0:
        r = temp % 10
        sum = sum + (r * r * r)   
        temp = temp // 10

    if sum == n:
        print(n, "is an Armstrong number")
