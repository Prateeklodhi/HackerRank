'''
In this code I am going to create a custome decorator where that decorator will be going to count the execution time of
the funciton that it take to execute, I will name it performance decorator....
'''
from time import time
def performance(function):
    def wrapper():
        start_time = time()
        function()
        endtime = time()
        duration = endtime-start_time
        print(duration)
    return wrapper

@performance
def loopto():
    for item in range(0,1000000000):
        item * 1

loopto()