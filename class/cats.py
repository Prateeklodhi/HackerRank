# Given the below class:
'''Excersice'''


class Cat:
    '''let's start over here'''
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

tom = Cat('Tom', 3)
meaow = Cat('Meaow', 4)
luis = Cat('luis', 1)

# 2 Create a function that finds the oldest cat


def oldest(cat_one, cat_two, cat_three):
    '''find the oldest cat'''
    if (cat_one.age > cat_two.age and cat_one.age > cat_three.age):
        return cat_one.name
    elif cat_two.age > cat_three.age and cat_two.age > cat_one.age:
        return cat_two.name
    else:
        return cat_three.name


def sort_method(*args):
    '''using args and max function to find out the oldest cat'''
    return max(args)
# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2


print(oldest(tom, meaow, luis))
print(sort_method(tom.age, meaow.age, luis.age))
