'''this program will tell about the dundar methods and there use'''
from typing import Any


class Toy(list):
    def __init__(self,color,age):
        self.color = color
        self.age = age
        self.object = {
            'name':'Hello'
        }
    def __str__(self) -> str:
        return f'Toy color is {self.color}'
    
    def __len__(self) -> int:
        return len(self.color)
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return str(self.color +' '+ str(self.age))
    
    def __getitem__(self,item):
        return self.object[item]

    def __add__(self,other)->int:
        return self.age+other.age

    def __sub__(self,other)->int:
        return self.age - other.age

    


action_figure = Toy('Red',5)
action_figure2 = Toy('Red',6)
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
print(action_figure+action_figure2)
print(action_figure-action_figure2)