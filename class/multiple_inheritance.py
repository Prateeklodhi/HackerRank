class User:
    def sign_up(self):
        print("Signup done!")

class Archer(User):
    def __init__(self,name,arrow_count) -> None:
        self.arrow_count = arrow_count
        self.name = name

    def arrows(self):
        print(f"{self.arrow_count} arrow's left")

class Wizard(User):
    def __init__(self,name,power) -> None:
        self.power = power
        self.name = name

    def powers(self):
        print(f"{self.power} powers left")

class Goblin(Archer,Wizard):
    def __init__(self, name, arrow_count,power) -> None:
        Archer.__init__(self,name,arrow_count)
        Wizard.__init__(self,name,power)


gone = Goblin("gone",123,10)
gone.sign_up()
gone.arrows()
gone.powers()