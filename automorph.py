"""
A number is called Automorphic number if its square ends in the same digits as the number itself.
Eg: 25 ^ 2 = 625
"""

"""
Example usage:
python automorph --n <To find if number is automorphic or not>
python automorph --n 3
OR 
DEFAULT DOES WORK
python automorph 
"""

import argparse
import sys


def square(n):
    return str(n**2)


def is_automorphic(n):
    square_num = str(square(n))
    str_n = str(n)
    return square_num.endswith(str_n)


def main(n):
    if is_automorphic(n):
        print("{} is Automorphic.".format(n))
        return
    print("{} is not Automorphic.".format(n))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Find check if number is automorphic or not.')
    parser.add_argument('-n', type=int,
                        help='Check Automorphism.', required=True)
    args = parser.parse_args()
    main(args.n)
