#Simple Calculater

Num1 = int(input("Enter First Number : "))
Num2 = int(input("Enter Second Number : "))

op = input("Choose the operations : (+,-,*,/,%) : ")

if op == '+':
    print("Addition : ",Num1 + Num2)
    
elif op == '-':
    print("Subtraction : ",Num1 - Num2)

elif op == '*':
    print("Multiplication : ", Num1 * Num2)

elif op == '/':
    if Num2 != 0:
        print("Division : ", Num1 / Num2)
    else:
        print("Division with Zero is not posible.")

elif op == '%':
    print("Reminder : ", Num1 % Num2)

else:
    print("Invalid Operation")
    

