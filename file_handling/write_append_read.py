'''
This code will demonstrate the use of the mode in open() there are different modes in an open function to read write and append something on the file.
and we use with to open a file the reason behind using keyword with is we do not need to close a file each time when we open it.
'''
with open('random_string.txt','+r')as txt_file:
    # when we use +r mode and write something on it, it start writing on to the at the begaining of the file and the data which is already in file got replaced character by character.
    text = txt_file.write("Hello") # return the number of character that is given to the function
    print(text) 

with open('sad.txt','w') as sad_file: # if there is no file name as sad.txt it will create new file.
    sad_file.write(":(")

with open('random_string.txt','a') as txt_file:
    txt_file.write(":)")