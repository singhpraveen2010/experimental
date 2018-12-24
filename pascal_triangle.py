from __future__ import division


def print_row(value_list, list_size):
    for _ in range(list_size):
        print " ",
    for value in value_list:
        print "%d " % value,
    print"\n"


def first_row(triangle_length):
    print_row([1], triangle_length)


def construct_pascal_triangle(triangle_length):
    if triangle_length <= 0:
        print "No triangle possible."
        return
    first_row(triangle_length)
    row_list = [1, 1]
    for _ in range(triangle_length):
        triangle_length -= 1
        row_len = len(row_list)
        temp_list = [1, 1]
        for index, value in enumerate(row_list):
            if index == row_len - 1:
                break
            temp_sum = value + row_list[index + 1]
            temp_list.insert(index + 1, temp_sum)
        print_row(row_list, triangle_length)
        row_list = temp_list[:]


def main():
    input_value = raw_input("Enter the length:: ")
    triangle_length = 7
    try:
        triangle_length = int(input_value)
    except Exception as e:
        print "Invalid integer using default."
    print "### The length of triange is ### %d " % triangle_length
    construct_pascal_triangle(triangle_length)

if __name__ == '__main__':
    main()
