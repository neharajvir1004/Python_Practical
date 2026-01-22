#Marksheet

Sub1 = int(input("Enter First Subject Marks : "))
Sub2 = int(input("Enter Second Subject Marks : "))
Sub3 = int(input("Enter Third Subject Marks : "))
Sub4 = int(input("Enter Fourth Subject Marks : "))

Total =((Sub1+Sub2+Sub3+Sub4)/4)
print("Total is ", Total)

Per = ((Sub1+Sub2+Sub3+Sub4)/4)
print("Percentage is ", Per)

if Per <= 99 and Per >= 80:
    print("Grade : A+")

elif Per < 8 and Per >= 70:
    print("Grade : A")

elif Per < 70 and Per >= 60:
    print("Grade : B+")

elif Per < 60 and Per >= 50:
    print("Grade : C")

elif Per < 50 and Per >= 40:
    print("Grade : D")

elif Per < 40 and Per >= 0:
    print("Grade : Fail")

else:
    print("Invalid Marks Entry")









