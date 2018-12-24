#Source: http://www.geeksforgeeks.org/juggler-sequence/

from math import (sqrt,
                  floor)

def is_even(number):
    return number % 2 == 0


def square_root(number):
    return sqrt(number)


def pow_3(number):
    return number**3


def floor_num(number):
    return int(floor(number))


def generate_juggler_series(number):
    print(number),
    while number != 1:
        temp = number
        if not is_even(number):
            temp = pow_3(number)
        temp = floor_num(square_root(temp))
        print temp,
        number = temp


def main():
    number = int(raw_input("Enter the starting integer of series:: "))
    if number <= 0:
        print("Only Works for positive integers.")
        return
    print("The juggler series of {} is").format(number)
    generate_juggler_series(number)


if __name__ == '__main__':
    main()
