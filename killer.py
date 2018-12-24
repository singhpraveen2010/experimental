def killed(people, not_kill):
    saved = []
    for person in people:
        if not_kill:
            saved.append(person)
        not_kill = not not_kill
    return saved, not_kill


def find(people, not_kill=True):
    while len(people) > 1:
        saved, not_kill = killed(people, not_kill)
        people = saved

    print "%d is alive!" % people[0]


def main():
    people = range(1, 101)
    find(people)


if __name__ == '__main__':
    main()
