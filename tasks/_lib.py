import numpy


def create_random_array(length=10):
    array = []

    for i in range(0, length):
        new_number = numpy.random.randint(-10, 10)
        array.append(new_number)

    # could yield
    return array


def print_array(array, print_func=lambda x: print(x, end=' ')):
    for item in array:
        print_func(item)


def build_triangle(height, offset=0):
    if offset < 0:
        raise Exception(f'Offset cant be less then zero but the value is {offset}')

    builder = []

    for line_index in range(1, height + 1):
        for _ in range(0, offset):
            builder.append(' ')

        for _ in range(0, height - line_index):
            builder.append(' ')

        for _ in range(0, line_index * 2 - 1):
            builder.append('*')

        builder.append('\n')

    return ''.join(builder)
