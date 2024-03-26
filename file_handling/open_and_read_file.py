file = open('random_string.txt') # by default a file opens in read mode
print('first  time file read ',file.read()) # to read the file 
# file.seek(0) # to rest the cursor at the zero position
print('second time file read',file.read()) # now it will read the file from the start again
file.seek(0)
print('read a line ',file.readline()) # to the a line
print('read all the line',file.readlines()) # to read multiple lines at onces and it returns a list.