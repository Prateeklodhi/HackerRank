# In python there is another use full module to create an array called array 
from array import array
list_of_numbers = [1,2,3,4,5,6,7,8,9]
new_array = array('i',list_of_numbers) # this array function takes typecode which can be found at https://docs.python.org/3/library/array.html link and it takes an iterable to convert it into an array...
# An array can only has homogenoues data within it.
print(new_array[5])