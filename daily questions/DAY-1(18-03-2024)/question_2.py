# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

def fact(number):
    return 1 if number == 0 else  number * fact(number-1)

print(fact(8))