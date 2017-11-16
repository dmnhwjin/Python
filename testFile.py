from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func")
        a_func()
        print("I am doing some boring work after executing a func")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decorating():
    """Hey yo ! decorate me"""
    print("I am the function which needs some decoration to remove my foul smell")

print(a_function_requiring_decorating.__name__)