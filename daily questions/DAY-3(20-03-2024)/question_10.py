'''Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:

hello world and practice makes perfect and hello world again
Then, the output should be:

again and hello makes perfect practice world'''

string = input("Enter an string:").split(' ')
for item in string:
    if string.count(item) > 1:
        # if item not in duplicate_item:
        string.remove(item) 
string.sort()
print(' '.join(string))