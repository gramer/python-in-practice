def index_word(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


def index_word_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


if __name__ == '__main__':
    address = 'Four score and seven years ago'
    result = list(index_word_iter(address))
    print(result[:3])
