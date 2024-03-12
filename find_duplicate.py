some_list = ['a', 'b', 'c', 'b', 'd', 'e', 'n', 'n']
new_list = []
for item in some_list:
    if some_list.count(item) > 1:
        # new_list.append(some_list.pop(some_list.index(item)))
        if item not in new_list:
            new_list.append(item)
print(new_list)
print(some_list)