'''
Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define an instance parameter, need add it in __init__ method.You can init an object with construct parameter or set the value later
'''
class Demo:
    name = "Hello"
    def __init__(self,name=None):
        self.name = name

demo = Demo("Prateek")

print(demo.name,Demo.name)