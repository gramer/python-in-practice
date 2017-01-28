def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs')


def divide_wrapper(a, b):
    try:
        result = divide(a, b)
    except ValueError:
        print("Invalid inputs {0}, {1}".format(a, b))
    else:
        print('Result is %.1f' % result)


if __name__ == '__main__':
    divide_wrapper(0, 0)
    divide_wrapper(1, 1)
