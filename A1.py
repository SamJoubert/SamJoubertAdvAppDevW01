# Program Name: A1.py
# Course: IT3883/Section W01
# Student Name: Sam Joubert
# Assignment Number: Lab1
# Due Date: 09/05/ 2025
# Purpose: The program first asks the user to select one of four options: append to an input
# buffer, clear the input buffer, display the contents of an input buffer, or exit the program.
# The user can input one of these four options, which will do as the description says.
# Resources: Module 1-1

#declares the input buffer
buffer = []

#loop for the user to continuously edit the input buffer
while True:
    #prints options to the user
    print("Please select one of the following options:")
    print("1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program\n")

    #user choice
    selection = input()

    #adds string of user's choice to the input buffer
    if selection == "1":
        print("Please input data to append: ", end="")
        buffer.append(input())
        print()

    #clears the input buffer
    elif selection == "2":
        buffer = []
        print("The input buffer is now empty")
        print()

    #prints the input buffer
    elif selection == "3":
        print(buffer)
        print()

    #exits the loop and ends the program
    elif selection == "4":
        print("Thank you for your time")
        break

    #catches inputs that are invalid
    else:
        print("Please select a valid option (1, 2, 3, 4)")
        print()