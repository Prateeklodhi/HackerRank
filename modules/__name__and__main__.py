'''
this file demonstrate the use of the __name__ and __main__
basically to find the name of the current python file name we use __name__
and __main__ is the main file that imports some of the package in it, it automatically becomes the main 
file.
'''
from shopping import shoppincart

print(__name__)
if __name__ == "__main__":
    print(shoppincart.__name__)