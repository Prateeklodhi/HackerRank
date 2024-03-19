'''
It's a special type of iterator that generates a value on the fly.
A generator is a function that is uesed to do a task on the fly without using extra memory space and time.
it help us to reduce the time of exceution of a statement.
a function become generator when that function has yield with it.
'''
def generator_function(num):
    for item in range(num):
        yield item

for item in generator_function(100):
    print(item)