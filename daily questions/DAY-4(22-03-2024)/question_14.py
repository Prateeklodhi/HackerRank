'''Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Suppose the following input is supplied to the program:

Hello world!
Then, the output should be:

UPPER CASE 1
LOWER CASE 9
'''

string = input("Enter your input:")
upper_case = 0
lower_case = 0
for char in string:
    if char.isupper():
        upper_case += 1
    if char.islower():
        lower_case += 1
print(f'UPPER CASE {upper_case}\nLOWER CASE {lower_case}')