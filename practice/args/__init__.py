import json


def decode_wrong(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default


def decode_right(data, default=None):
    """Load JSON data from a string

    :param data: JSJON data to decode
    :param default: Value to return if decoding fails.
     Defaults to an emtpy dictionary.
    :return:
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default


def safe_division(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_div = kwargs.pop('ignore_zero_div', False)

    if kwargs:
        raise TypeError('Unexpected **kwargs: %r' % kwargs)

    try:
        return number / divisor
    except ZeroDivisionError:
        if ignore_zero_div:
            return float('inf')
        else:
            raise
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
