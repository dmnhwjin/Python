from functools import wraps

def decorator_name(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        if not can_run:
            return "Funtion will not run"
        return f(*args,**kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

# can_run=True
#
# print(func())
#
# can_run=False
#
# print(func())


def logit(func):
    @wraps(func)
    def with_logging(*args,**kwargs):
        print(func.__name__+" was called")
    return with_logging

@logit
def addition_func(x):
    """ do some match."""
    return x + x


result=addition_func(4)