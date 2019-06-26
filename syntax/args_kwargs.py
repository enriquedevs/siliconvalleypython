
def sum_arguments(*args):
    return sum(args)


print(sum_arguments(4, 7, 2, 3, 5, 6, 1))


def print_dictionary(**kwargs):
    print(kwargs)


print_dictionary(hello='hi', my_number=23, my_float= 12.7)


def generic_method(*args, **kwargs):
    print(args)
    print(kwargs)


generic_method(2, 'hi', 23, 19.3, True, regards='hello', batman=True, my_float=28.3)