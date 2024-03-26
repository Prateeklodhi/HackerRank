'''
in this we are going to demonstrate the use of the pdb python debug a built in module in python to test the python file.
'''

import pdb

def add_two_numbers(number_one,number_two):
    pdb.set_trace() # it hold the program on this line and let us do testing on various option which we can run on the command line
    pdb.main()
    return number_one + number_two

add_two_numbers(4,'a')


'''
for more go through with this link
'''