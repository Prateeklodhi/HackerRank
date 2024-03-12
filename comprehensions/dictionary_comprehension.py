'''
A dictionary comprehension is a way to create a dictionary using short hand sytex.

'''

my_dict = {"Key_"+str(number):number*2 for number in [1,2,3] }
print(my_dict)

my_dict2 = {
    "hello" : "world",
    1 : "get"
}
for key,value in my_dict.items():
    print(key,value)