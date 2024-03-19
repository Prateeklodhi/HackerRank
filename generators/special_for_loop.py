'''
In this program we will be going to create our own for loop a special for loop using next call,
there will be a function that takes an iterable and we will iter function to iterate through that 
iterable.
'''
def special_for(iterable):
    iterable = iter(iterable)
    while True:
        try:
           print(next(iterable))
        except StopIteration:
            break

my_list = range(1,11)
special_for(my_list)
