'''
this python file demonstarts the use to try except in the file and tell you about the type of exception that can be raised while doing file handling..
'''

try:
    with open('sad.txt','1') as file:
        print(file.read())
except FileNotFoundError as err:
    print(err)
except IOError as err:
    print(err)
except Exception as err:
    print(err)