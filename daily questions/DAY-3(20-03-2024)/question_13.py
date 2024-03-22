'''Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3'''

string = input("Enter your string:").strip(' ')
print(string)
DIGITS = 0
LETTERS = 0
for char in string:
    if char.isnumeric():
        DIGITS += 1
    elif char.isalpha():
        LETTERS += 1
print(f'LETTERS:{LETTERS}\nDIGITS:{DIGITS}')