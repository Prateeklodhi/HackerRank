'''
To take input at the command line excecution we can use sys.argv.
'''
import sys

name = sys.argv[1] # 0 is reserved for the file name
print('Hello',name)