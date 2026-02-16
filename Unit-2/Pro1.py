# Basic Exception Handling Example

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

except Exception as e:
    print("Something went wrong:", e)

print("Program continues...")
