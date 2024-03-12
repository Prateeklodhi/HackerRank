'''
A decorator is a function that take a function as an input and to create a decorator function we have to follow a proper syntex that is a High order function and then a wrapper function in it then the calling of the function which is passed in it as an input.
'''
def my_decorator(function):
    def wrap_function():
        try:
            i = 1
            j = i / 0
            function()
        except :
            print("Hmmm...! something went wrong hunnnn...")
    return wrap_function

@my_decorator # ? to use a decorator we have to use the @ operator
def hello_call():
    print("Hello world of decorators...")


hello_call()