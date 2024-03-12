some_list = ['a','b','b','c','d','e','e']
duplicate_list = {item for item in some_list if some_list.count(item) > 1 }
print(duplicate_list)