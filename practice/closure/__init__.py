def create_multipliers():
    return [lambda x, i=i: i * x for i in range(5)]