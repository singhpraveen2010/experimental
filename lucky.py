"""
A number is called lucky a number if if all digits of the number are different.
Eg: 123
"""

"""
Example usage:
python lucky --n <To find if number is lucky or not>
python lucky --n 123
OR 
DEFAULT DOES WORK
python lucky 
"""

import argparse
import sys
from collections import Counter


def is_lucky(n):
    str_n = str(n)
    num_set = set(str_n)
    return len(num_set) == len(str_n)


def find_frequency(n):
    digit_frequency = Counter()
    str_n = str(n)
    for digit in str_n:
        digit_frequency[digit] += 1

    for digit in digit_frequency:
        frequency = digit_frequency[digit]
        if frequency > 1:
            print "{} occurs {} times.".format(digit, frequency)


def main(n):
    if is_lucky(n):
        print("{} is a Lucky Number.".format(n))
        return
    print("{} is not a Lucky Number.".format(n))
    find_frequency(n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Check if number is lucky or not.')
    parser.add_argument('-n', type=int,
                        help='Lucky.', required=True)
    args = parser.parse_args()
    main(args.n)
