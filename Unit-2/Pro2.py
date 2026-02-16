# Creating user-defined exception

class InvalidAge(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAge("Age must be 18 or above.")

    print("Access granted.")

except InvalidAge as e:
    print("Error:", e)

except ValueError:
    print("Please enter a valid number.")
