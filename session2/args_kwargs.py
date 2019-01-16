def my_method(arg1, arg2):
    return arg1+arg2

my_method(5, 6)

def my_long_method(arg1, arg2, arg3, arg4, arg5, arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6

def addition_simplified(*args):
    return sum(args)

addition_simplified(3, 5, 2, 12, 24, 55)

##

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(12, 34, 56, name='Jose', location='UK')

#Therefore allows multiple arguments to be passed even if you don't know what's coming
