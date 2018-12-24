def toggle(doors):
    l = len(doors)
    for i in range(1, l + 1):
        for j in range(1, l, i):
            doors[j] = not doors[j]
    return doors


def print_open(doors):
    l = len(doors)
    n = range(l)
    for i, j in zip(doors, n):
        if i == False:
            print j - 1


def main():
    doors = [True] * 100
    toggled_doors = toggle(doors)
    print_open(toggled_doors)


if __name__ == '__main__':
    main()
