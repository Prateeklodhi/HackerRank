'''In this python file you are going to see the use of inheritance.'''
class Pet:
    '''This is the perant class'''
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def jump(self)->str:
        '''simple function return a string only'''
        return "No! I can't jump."

    def attack(self) -> str:
        '''return strings with variables'''
        return f"Hi my name is {self.name} and I can attack,My age is {self.age} Years"

class Cat(Pet):
    '''Child class'''
    def meaou(self):
        '''Just say meaou'''
        return "Meaou"


citty = Cat("Citty",2)
print(citty.jump())
print(citty.attack())
print(citty.meaou())
