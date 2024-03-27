'''
in this python file we are going to demonstrate how to use the file path...
there are two types of path available ...
1. absolute path.
2. relative path.
'''
import os
# absolute path from the base directory to the file directory is called the absolute path.
os.path
with open('i:/My Drive/Python/JustForFun/file_handling/file_path.py','r') as sad_file:
    file = sad_file.read()
    print(file)

# relative path from the current directory to the file is called relative.
with open('./file_handling/sad.txt','r') as sad_file:
   file =  sad_file.read()
   print(file)