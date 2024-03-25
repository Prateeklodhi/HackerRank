'''
there is one more module called collection module that has operations releted to dictionary.
'''
from collections import Counter, defaultdict, OrderedDict # in python 3.7 and above there is no need to add OrderedDict

#the counter function help us to find the number number of duplicate values it makes the value as key and it's occurance value in an iterable.
list_of_numbers = [1,2,3,4,5,6,7,7,3,5,1,6,7,3,1,5,7,2,1,]
dictionary = {"key":"hello","value":"hey","hey":"hello","key":"hey"}
print(Counter(list_of_numbers))
# Counter({1: 4, 7: 4, 3: 3, 5: 3, 2: 2, 6: 2, 4: 1}) // output

# the defaultdict function is used to add a default value to the dictionary if there is no such key found. it takes a function as first argument

dictionary = defaultdict(lambda : 5,dictionary) # it returns a new dictionary based on the dictionary passed as second argument.
print(dictionary["eh"])
