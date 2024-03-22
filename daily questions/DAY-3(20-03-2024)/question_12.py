'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''

all_evan = []
for string in range(1000,3001):
    counter = 0
    for char in str(string):
        if int(char)%2 == 0:
            counter+=1
    if len(str(string))==counter:
       all_evan.append(str(string))
print(','.join(all_evan))

print(','.join([str(item) for item in range(1000,3001)if all(map(lambda i: int(i)%2==0,str(item)))]))
