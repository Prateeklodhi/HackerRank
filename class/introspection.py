'''
    A introspection mean : showing all the methods and variables related to an object
    and the key used to do such opertaion is "dir".
'''


class User:
    '''It's a super class haveing function name sign_up'''

    def sign_up(self) -> str:
        '''this function will return a string'''
        return "User signed in."

    def attack(self) -> str:
        '''This function will return a string'''
        return "No power's activated yet!"


class Wizard(User):
    '''This is a drived class inheritated User class'''

    def __init__(self: object, name: str, power: str) -> None:
        self.name = name
        self.power = power

    def attack(self) -> str:
        '''This function will return a string'''
        return f"Wizard name: {self.name} and he is having power of {self.power}."


class Goblin(User):
    '''this is a drived class inheritated User class'''

    def __init__(self, name: str, power: str) -> None:
        self.name = name
        self.power = power


class Archer(User):
    '''This is a drived class inheritated User class'''

    def __init__(self: object, name: str, power: str) -> None:
        self.name = name
        self.power = power

    def attack(self) -> str:
        '''This function will return a string'''
        return f"Archer name: {self.name} and he is having power of {self.power}."


wiz = Wizard('Miler', '50')
gob = Goblin('Buk', '0')
arch = Archer("Balina", '100')
print(dir(arch))  # doing introspection of arch object.
