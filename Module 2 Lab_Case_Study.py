#Author: Stephanie Guerrero
#App Name: Student Awards
#This app is used to determine is a student is eligible for an award based on their GPA. The user will input the student's last name, first name, and GPA.




while True: #this loop will continue to run until user enters the exit code of "ZZZ"
    last_name = input("Enter student's last name:")#user will input the student's last name
    
    if last_name == "ZZZ":#if the user enters exit code "ZZZ" the program will print a message and break the loop
        print("You have entered an exit code. Exiting program.")
        break
    
    else:#if the user doesn't enter the exit code, the program will continue to ask for the student's first name and GPA
        
        first_name = input("Enter student's first name:")#user inputs student's first name
        gpa = float(input("Enter student's GPA:"))#user inputs student's GPA
        
        if gpa >= 3.5:
            print(f"{first_name} {last_name}: Congratualtions! You made the Dean's List!")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name}: Congratulations! You made the Honor Roll!")
        else:
            print(f"{first_name} {last_name}: Your GPA is too low to receive an award, but keep trying!"