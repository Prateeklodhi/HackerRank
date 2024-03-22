'''Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9
Then, the output should be:

11106'''
from functools import reduce
# let's take an input digit
num = input("Enter a number:")
sum_of_digit = reduce(lambda num,accu: int(num)+int(accu),[num*i for i in range(1,5)])
# for number in range(1,5):
#     sum_of_digit = sum_of_digit + int(str(num)*number)

print(sum_of_digit)