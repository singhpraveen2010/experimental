"""A number N is fibonacci if atleast one of  these values (5*N^2+4) or (5*N^2-4) is a prefect square."""

from math import sqrt
import sys


def check_prefect_square(n):
    sq = int(sqrt(n))
    return sq * sq == n


def check_fibo(n):
    temp = 5 * n**2
    return check_prefect_square(temp + 4) or check_prefect_square(temp - 4)


def main():
    n = int(raw_input("Enter number to check:: "))
    if n < 0:
        print("Not Fibnacci number")
        sys.exit(1)
    print check_fibo(n)


if __name__ == '__main__':
    main()
