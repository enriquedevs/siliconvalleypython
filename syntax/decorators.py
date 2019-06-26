
import functools


def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print('before')
        func()
        print('after')
    return function_that_runs_func


@my_decorator
def my_function():
    print('hello')


my_function()


def my_decorator_with_param(number):
    def my_decorator_func(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print('before')
            if number == 56:
                func(*args, **kwargs)
            else:
                print('not running function')
            print('after')
        return function_that_runs_func
    return my_decorator_func


@my_decorator_with_param(56)
def my_new_function(message, country='France'):
    print(message, country)


my_new_function('bonjour')
