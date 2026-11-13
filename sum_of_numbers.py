#!/usr/bin/python3
# Created by Mignonne Gihozo
# Created on 2026-11-13
# This program calculates the sum of numbers using a while loop


def main():
    # this function calculates the sum of numbers using a while loop

    # input
    user_input = input("Enter a positive integer: ")
    print("")

    # process & output
    try:
        user_number = int(user_input)

        if user_number < 0:
            print(f"{user_input} is not a positive integer.")
        else:
            sum_of_numbers = 0
            counter = 0

            while counter <= user_number:
                sum_of_numbers = sum_of_numbers + counter
                counter = counter + 1

            print(f"The sum of numbers from 0 to {user_number} is {sum_of_numbers}.")
    except ValueError:
        print(f"{user_input} is not a valid integer.")

    print("Thank you for using this program. Goodbye.")


if __name__ == "__main__":
    main()
