# coding=utf-8
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)


def normalize(numbers):
    """ iterator 에 대한 방어적이지 못한 경우

    단점 : for loop 가 실행되지 않는다.
    """
    total = sum(numbers)
    result = []
    for v in numbers:
        percent = 100 * v / total
        result.append(percent)
    return result


def normalize_copy(numbers):
    """ generator 에 대한 list 로 copy 한 코드

    단점 : 메모리 효율적이지 못한 경우
    """

    numbers = list(numbers)
    total = sum(numbers)
    result = []
    for v in numbers:
        percent = 100 * v / total
        result.append(percent)
    return result


def normalize_func(get_iter):
    """ lambda 를 이용하여 callback 하는 경우

    단점 : 코드가 지저분함
    """
    total = sum(get_iter())
    result = []
    for v in get_iter():
        percent = 100 * v / total
        result.append(percent)
    return result


def normalize_defensive(numbers):
    """ 추천하는 방어적인 코등 방법 """
    if iter(numbers) is iter(numbers):
        raise TypeError('Must supply a container')

    total = sum(numbers)
    result = []
    for v in numbers:
        percent = 100 * v / total
        result.append(percent)
    return result


class ReadVisits(object):
    """ recommended: 이터러블 컨테이너를 이용한 방법 """
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)
