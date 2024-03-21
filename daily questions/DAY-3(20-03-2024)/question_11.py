'''Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

Example:

0100,0011,1010,1001
Then the output should be:

1010
Notes: Assume the data is input by console'''
while True:
    try: 
        list_of_number = []
        four_val = input('Enter your values:').split(',')
        print(len(four_val))
        if len(four_val) > 4 :
            raise Exception('Can not enter more then four values')
        list_of_number  =','.join([ value for value in four_val if int(value,2)%5 == 0 ])
        print(''.join(list_of_number))
    except Exception as Error:
        print('Try again...\n')
    else:
        break
