#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: December 2019
# This program calculates the average of an array


import random


def calculate(list_of_numbers):
    # this function calculates the average in a 2D array

    # variables
    divider = 0
    sum_of_numbers = 0

    # process
    for row_value in list_of_numbers:
        for counter in row_value:
            sum_of_numbers = sum_of_numbers + counter
            divider += 1

    average = sum_of_numbers/divider
    return average


def main():
    # This function generates random numbers then prints the average

    # Variables and lists
    number_list = []

    # Input
    rows = int(input("How many numbers in each row? "))
    columns = int(input("How many numbers in each list? "))
    print("")

    # Process
    for counter in range(0, rows):
        temporary_column = []
        print("Row {0}:".format(counter + 1))
        for counter in range(0, columns):
            random_number = random.randint(0, 50)
            temporary_column.append(random_number)
            print(random_number)
        number_list.append(temporary_column)
        print("")

    average = calculate(number_list)

    # Output
    print("The average of the numbers is", average)


if __name__ == "__main__":
    main()
