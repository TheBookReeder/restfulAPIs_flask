import functools

def my_decorator(func):
    @functool.wraps(func)
    def functions_that_runs_func():
        print("In the decorator!")
        func()
        print("After the decorator!")
    return function_that_runs_func

@my_decorator
def my_function():
    print("I'm the function!")

my_function()

##

def decorator_with_args(number):
    def my_decorator(func):
        @functools_wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("in the decorator!")
            if number == 56:
                print("Not running the function")
            else:
                func(*args, **kwargs)
            print("after the decorator!")
        return function_that_runs_func
    return my_decorator

@decorator_with_args(56)
def my_function_too(x, y):
    print(x+y)

my_function_too(57, 67)
