'''
The reduce function is used to to reduce a iterable and return a value it takes three arguments,
first is function second is the iterable and the last is initial. To use the reudce function one have to
import reduce form the functools.
'''

from functools import reduce    
# my_list = [1,2,3,4,5]
# second_list = [11,4,3,2,1]
# def sum_of_numbers(start,items):
#     return start + items

# print(reduce(sum_of_numbers,my_list)) 

#1. Write a Python function using the reduce function to calculate the sum of squares of a list of numbers.
number_list = [5,3,2,1,4]

# if accumlator is not given then the result is 35
print(reduce(lambda acc,num: acc +(num**2),number_list))
# First iteration: sum_of_squares(5, 3) gives 5 + 3**2 = 14
# Second iteration: sum_of_squares(14, 2) gives 14 + 2**2 = 18
# Third iteration: sum_of_squares(18, 1) gives 18 + 1**2 = 19
# Fourth iteration: sum_of_squares(19, 4) gives 19 + 4**2 = 35

# if accumlator ( 0 ) is given then the result is 55
print(reduce(lambda acc,num: acc +(num**2),number_list,0))
# First iteration: sum_of_squares(0, 5) gives 0 + 5**2(25) = 25
# Second iteration: sum_of_squares(25, 3) gives 25 + 3**2(9) = 34 
# Third iteration: sum_of_squares(34, 2) gives 34 + 2**2(4) = 38
# Fourth iteration: sum_of_squares(38, 1) gives 38 + 1**2(1) = 39
# Fourth iteration: sum_of_squares(39, 4) gives 39 + 4**2(16) = 55

#2. Create a function that utilizes the reduce function to find the product of a list of numbers.
print(reduce(lambda acc,item: acc*item,number_list,1))

# Write a Python function to concatenate a list of strings into a single string using the reduce function.
string_list = ["p","r","a","t","e","e","k"]
print(reduce(lambda accu, item: accu + item , string_list))

# Develop a function that employs the reduce function to find the maximum element in a list of numbers.
print(reduce(lambda acc,item: acc if acc > item else item , number_list ))  