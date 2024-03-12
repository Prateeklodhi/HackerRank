'''
A map function is a function that takes two arguments first is a function and another is
an iterable, an returns a map object as an output that can be converted to any iterable.
'''

def multiple_by_two(item):
    return item * 2 

my_list = [9,8,7,6,5,4,3,2,1]
my_list.reverse()
print(list(map(multiple_by_two,my_list)))