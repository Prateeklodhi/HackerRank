"""Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use init method to construct some parameters"""

class Main:
    def __init__(self,string):
        self.string = string

    def getString(self):
        self.string = input("Enter a string")

    def printString(self):
        print(self.string)


main = Main("hello")
main.printString()