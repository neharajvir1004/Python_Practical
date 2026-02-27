#Write a program to do student operations using menu as follows
#a) Add Student
#b) Search Student
#c) List All Students
#d) Update Student
#e) Delete Student
#f) Exit

students = {}

while True:
    print("\n--- Student Menu ---")
    print("a) Add Student")
    print("b) Search Student")
    print("c) List All Students")
    print("d) Update Student")
    print("e) Delete Student")
    print("f) Exit")
    
    choice = input("Enter your choice: ")

    # Add Student
    if choice == 'a':
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        students[roll] = name
        print("Student added successfully!")

    # Search Student
    elif choice == 'b':
        roll = input("Enter Roll No to search: ")
        if roll in students:
            print("Name:", students[roll])
        else:
            print("Student not found!")

    # List All Students
    elif choice == 'c':
        if students:
            print("\nStudent List:")
            for roll, name in students.items():
                print("Roll No:", roll, "Name:", name)
        else:
            print("No students available.")

    # Update Student
    elif choice == 'd':
        roll = input("Enter Roll No to update: ")
        if roll in students:
            name = input("Enter new Name: ")
            students[roll] = name
            print("Student updated successfully!")
        else:
            print("Student not found!")

    # Delete Student
    elif choice == 'e':
        roll = input("Enter Roll No to delete: ")
        if roll in students:
            del students[roll]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    # Exit
    elif choice == 'f':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
