'''
_Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*

Note: i=0,1.., X-1; j=0,1,¡ ­y-1. Suppose the following inputs are given to the program: 3,5

Then, the output of the program should be:

[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''

row_count = int(input("Enter x:"))
col_count = int(input("Enter y:"))
list_two_d = []
for row in range(row_count):
    inner_list = []
    for col in range(col_count):
        inner_list.append(col*row)
    list_two_d.append(inner_list)

print(list_two_d)