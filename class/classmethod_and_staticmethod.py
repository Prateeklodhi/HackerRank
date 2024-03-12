'''Demostration of class method'''


class Demo:
    '''let's start'''

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    # creating a decorator using classmehtod

    @classmethod
    def decor(cls, name, age):
        '''a class method recive a class as an implicit first argument'''
        return f"Oh your name is {name}, Ok yor are {age} year's old"

    @staticmethod
    def static(obj: object) -> str:
        '''A static method do not required a class an implicit first argument'''
        return f"{obj.name} and {obj.age}"


object_one = Demo("Hello", 23)
print(Demo.decor("Pranjali", 21))
print(Demo.static(object_one))
