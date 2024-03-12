'''
A lambda experssion is used to make a function that will not be used further, small oneline function that will be used 
in a instant way and after the action it will be destoryed.
for example I want an action to be performed i.e. find the suqare of a number and I want to do that once only. in such case
I'll lambda experssion.
Example:
        def suqare(item): // without lambda
            return item ** 2
        print(suqare(5))
        print(lambda item : item ** 2) with lambda
'''

my_list = [5,4,3]
print(list(map(lambda item: item**2,my_list)))


suff_list = [("A",8),("T",9),("Q",29),("L",17),("Y",19)]
suff_list.sort(key= lambda second_index_item:second_index_item[1])
print(suff_list)