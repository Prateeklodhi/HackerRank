'''A program to demostrate the use of abstraction'''


class Player:
    ''' This class contain one constructor and one function in it.'''

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def _run(self) -> str:
        '''This run function basically return a string message'''
        return f'Hello {self.name} oh your age is {self.age}'


player_one = Player('leon', 25)
player_one._run = 'hello'
print(player_one._run) # a method can not be private in python but for the need of OOPs we use _to define the private member in python it can not be strictly implemented
