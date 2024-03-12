'''
A pure function is a function that do not intract with the outer world code,
And a pure function must take the same input and result same output like it's taking 
a List as an input then it will return a list an output.
'''

def pure_function(a_list):
    square = []
    for _ in a_list:
        square.append(_*2)
    # print(square) exposed to the outer world if we use print over here.
    return square

print(pure_function([1,2,3]))