from math import pow


def find_repeat(number):
    count = 1
    n = number
    if number >= 10:
        n = int(str(number)[-1])
    m = -1
    while True:
        value = int(pow(number, count + 1))
        str_value = str(value)
        m = int(str_value[-1])
        if n == m:
            break
        count += 1
    return count


def main():
    number = raw_input("## Enter number:: ")
    number = int(number)
    diff = find_repeat(number)
    print "\n## Repeatition count:: %d" % diff

if __name__ == '__main__':
    main()
