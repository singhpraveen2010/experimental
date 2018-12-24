"""
Example usage:
python event_average --n <To find the nth Carol number>
python carol --n 3
OR 
DEFAULT
python event_average 
"""

from __future__ import division
import argparse


def carol_formula(n):
    return int((2**n - 1)**2 - 2)


def carol_property(n):
    if n < 0:
        return "Undefined"
    if n == 1:
        return -1
    elif n == 2:
        return 7
    carol_str = '1' * (n - 2) + '0' + '1' * (n + 1)
    return int(carol_str, 2)


def get_suffix(n):
    suffix = "th"
    if n == 1:
        suffix = "st"
    elif n == 2:
        suffix = "nd"
    return suffix


def test():
    n_list = range(1, 8)
    for n in n_list:
        suffix = get_suffix(n)
        carol_f = carol_formula(n)
        carol_p = carol_property(n)
        assert carol_f == carol_p
        print("The {}{} Carol number is:: {}".format(n, suffix, carol_f))


def main(n):
    if n is None:
        test()
    else:
        suffix = get_suffix(n)
        print("The {}{} Carol number is:: {}".format(
            n, suffix, carol_property(n)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Find the nth Carol number or test the Carol series..')
    parser.add_argument('--n', metavar='Nth carol', type=int,
                        help='To find the nth carol number.')
    args = parser.parse_args()
    main(args.n)
