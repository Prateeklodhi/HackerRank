'''
This function is same as map but it do not return the exact number of input as output rather than it
returns the filtered output based on a condition..
'''
def only_odd_number(items):
    return items if items % 2 != 0 else False


my_list = [9,8,7,6,5,4,3,2,1]
print(list(filter(only_odd_number,my_list)))