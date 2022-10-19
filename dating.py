#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Oct 18 2022
# This program asks the user for their age it then determines if their age is in the likings of the grandparents

def main():

    # Get the users age
    user_num_string = input("Enter your age: ")

    # An try catch to catch any errors if they enter a string
    try:
        user_num = int(user_num_string)
        print("Hello")
    except Exception:
        print("Please enter a number")
    else:
    # A if statement to see if they are greater than or equal to 25 and less then or equal to 40
        if user_num >= 25 and user_num <= 40:
            print("You can date the grandchild")
        else:
            print("You can't date the grandchild")

if __name__ == "__main__":
    main()
