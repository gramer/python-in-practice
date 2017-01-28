def sort_priority1(values, group_):
    def helper(x):
        if x in group_:
            return 0, x
        return 1, x

    values.sort(key=helper)


def sort_priority2(values, group_):
    found = False

    def helper(x):
        if x in group_:
            found = True
            return 0, x
        return 1, x

    values.sort(key=helper)
    return found


def sort_priority3(values, group_):
    found = [False]

    def helper(x):
        if x in group_:
            found[0] = True
            return 0, x
        return 1, x

    values.sort(key=helper)
    return found[0]


class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return 0, x
        return 1, x


if __name__ == '__main__':
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    sort_priority1(numbers, group)
    print(numbers)
