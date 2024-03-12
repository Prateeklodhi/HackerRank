'''A demostration of class and objects '''
class Demo:
    '''A class name demo it has one constructor and one run method'''
    class_object_attribute = False
    def __init__(self,name:str,age:int) -> None:
        '''class constructor'''
        self.name = name
        self.age = age
        # Two ways to access a class object attribute
        # print(Demo.class_object_attribute)
        # print(self.class_object_attribute)

    def run(self)->str:
        '''Return's a string with the name and age'''
        # wrong way to access a constructor variable
        #print(Demo.name)
        return f"Hello {self.name}, Ohh you are {self.age} year's old!"
        # return self
D1 = Demo("Prateek",25)
print(D1)
demoObject = Demo("MyValue",25).run()
print(demoObject)
# print(demoObject.class_object_attribute)
# demoObject.class_object_attribute = True # class object cant not be changed.

# print(D1.run().run())
# print(D1.class_object_attribute)
