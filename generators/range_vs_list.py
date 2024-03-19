'''
in this program we will demostrate the use of generators. using the range() and a list[]
'''
import time
def performance(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(end-start)
    return wrapper

@performance
def loop_range(num):
    print("running range:")
    for item in range(num):
        item*10

@performance
def loop_list(num):
    print("running list:")
    for item in list(range(num)):
        item * 10

loop_range(900000000)
loop_list(900000000)# gives a MemoryError

