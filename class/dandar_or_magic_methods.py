'''This file will help out to understand the use of dandar methods'''


class User():
    '''Overriding few of dandar methods '''

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Overridding the str dandar {self.name}"

    def __len__(self) -> int:
        return len(self.name)

    def __mydan__(self) -> str:
        return f"Overridding the str dandar {self.name}  {len(self.name)}"


user = User("Prateek")
print(len(user))
print(str(user))
print(user.__mydan__())
