from functools import wraps
def type_logger(func):
    @wraps(func)
    def d_logger(*args):
        for i in args:
            print(f'{i} is {type(i)}', end=", ")
        return func(*args)
    return d_logger

@type_logger
def calc_cube(*args):
    """This is __doc__"""
    return list(map(lambda x: x ** 3, args))

a = calc_cube(5, 6)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)