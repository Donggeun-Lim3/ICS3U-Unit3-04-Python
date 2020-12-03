#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This program checks the number is positive, negative or 0

def main():

    # input
    your_number = int(input("Enter the number "))
    print("")

    # process
    if your_number > 0:
        # output
        print("The number is positive")
    elif your_number < 0:
        print("The number is negative")
    else:
        print("The number is 0")


if __name__ == "__main__":
    main()
