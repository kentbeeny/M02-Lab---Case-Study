#Kent Beeny
#SDEV 220
#M02 Lab - Case Study: if...else and while
#11/6/23
#This program will allow the user to enter student names
#and GPAs. The program will tell the user if the student
#qualifies for either the Dean's List or Honor Roll

fName = "GenericFirstName"
lName = "GenericLastName"
GPA = 6.0

while True:
    fName = input("Enter the student's First Name: ")
    lName = input("Enter the student's Last Name: ")
    while True:
        try:
            GPA = float(input("Enter the student's GPA: "))
            break
        except ValueError:
            print("That was not a valid GPA. Try again...")
    if lName == "ZZZ":
        break
    elif GPA >= 3.5:
        print(fName + " " + lName + " has made the Dean's List!")
    elif GPA >= 3.25:
        print(fName + " " + lName + " has made the Honor Roll!")
    else:
        print("This student has not made Dean's list or Honor roll.")
