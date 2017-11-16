import pdb

def test_var_args(f_arg,*argv):
    print("First normal arg:",f_arg)
    for arg in argv:
        print("another arg through *argv:",arg)

def greet_me(**kwargs):
    for key,value in kwargs.items():
        print("{0} =={1}".format(key,value))

def test_args_kwargs(arg1,arg2,arg3):
    print("arg1:",arg1)
    print("arg2:",arg2)
    print("arg3:",arg3)

def make_bread():
    pdb.set_trace()
    return "I don't have time"
#print(make_bread())

def generator_function():
    for i in range(10):
        yield i

# for item in generator_function():
#     print(item)


def fibon(n):
    a=b=1
    for i in range(n):
        yield a
        a,b=b,a+b

# for x in fibon(1000000):
#     print(x)


def generator_function():
    for i in range(3):
        yield i

# gen=generator_function()
# print(next(gen))
# print(next(gen))
# print(next(gen))


# print(next(gen))

def multiply(x):
    return(x*x)

def add(x):
    return(x+x)

funcs=[multiply,add]

# for i in range(5):
#     value=list(map(lambda x:x(i),funcs))
#     print(value)

# number_list=range(-5,5)
# less_than_zero=list(filter)

#
# def hi(name="yasoob"):
#     print("NOw you are inside the hi() function")
#
#     def greet():
#         return "Now you are in the greet() function"
#
#     def welcome():
#         return "Now you are in the welcome() function"
#
#     print(greet())
#     print(welcome())
#     print("Now you are back in the hi() fuction")
#
# hi()
# def hi(name="yasoob"):
#     def greet():
#         return "Now you are in the greet() fuction"
#
#     def welcome():
#         return "Now you are in the welcome() function"
#
#     if name=="yasoob":
#         return greet
#
#     else:
#         return welcome
#
# a=hi()
# print(a)
# print(a())


# def hi():
#     return "hi yasoob!"
#
# def doSomethingBeforeHi(func):
#     print("I am doing some boring work before executing hi()")
#     print(func())
#
# doSomethingBeforeHi(hi)


def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before ")

        a_func()

        print("I am doing some boring work after executing a_func")

    return wrapTheFunction


def a_function_requiring_decoration():
    print("I am the function which needs some decroation to remove")


a_function_requiring_decoration()

a_function_requiring_decoration=a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()

