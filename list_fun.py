li = [1,2,3,4,6]
listTwo = ['p','r','a','t','e','e','k']
name  =  ('').join(listTwo)
cpylistTwo = listTwo# reference variable 
cpylistTwo[0]="t"
print(cpylistTwo)
print(listTwo)
cpy2listtwo = listTwo[:]
cpy2listtwo[0] = 'p'
print(cpy2listtwo)
print(listTwo)

# print(name)
# when you do list slicing you can assign the sliced value to a variable.
# sliced_list = listTwo[:-1:]
# print(sliced_list)
# sliced_list = listTwo[::-1]
# print(sliced_list)
# sliced_list = listTwo[-1::-1]
# print(sliced_list)
# sliced_list = listTwo[-1:-3:-1]
# print(sliced_list)
