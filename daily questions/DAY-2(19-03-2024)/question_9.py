'''Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:

Hello world
Practice makes perfect
Then, the output should be:

HELLO WORLD
PRACTICE MAKES PERFECT'''

list_item = []
while True:
    string = input()
    if string == '0':
        break
    list_item.append(string.upper())

for item in list_item:
    print(item)