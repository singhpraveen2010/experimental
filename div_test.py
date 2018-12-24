from __future__ import division


def check_div_3(number):
    sum_c = 0
    while(number > 0):
        value = number % 10
        sum_c += value
        number = int(number / 10)
    return sum_c % 3 == 0


def check_div_11(number):
    sum_even = 0
    sum_odd = 0
    odd = True
    while(number > 0):
        value = number % 10
        if odd:
            sum_odd += value
        else:
            sum_even += value
        odd = not odd
        number = int(number / 10)
    diff = sum_odd - sum_even
    return diff % 11 == 0


def check_div_999(number):
    str_num = str(number)
    sum_c = 0
    str_len = len(str_num) - 1
    for index in range(str_len, -1, -3):
        start = index - 2
        if start < 0:
            start = 0
        num = int(str_num[start:index + 1])
        sum_c += num
    return sum_c % 999 == 0


def main():
    print("\n--- For 3 ---")
    num_list = [3, 9, 1332, 769452, 123456758933312]
    for number in num_list:
        if check_div_3(number):
            print("Divisible by 3")
        else:
            print("Not divisible by 3")

    print("\n--- For 11 ---")
    num_list = [76945, 11, 123]
    for number in num_list:
        if check_div_11(number):
            print("Divisible by 11")
        else:
            print("Not divisible by 11")

    print("\n--- For 999 ---")
    num_list = [235764, 1244633121, 9]
    for number in num_list:
        if check_div_999(number):
            print ("Divisible by 999")
        else:
            print ("Not divisible by 999")


if __name__ == "__main__":
    main()
