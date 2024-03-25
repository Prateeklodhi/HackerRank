'''
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:

ABd1234@1
'''

password_list = input().split(',')
zero_to_nine = ''.join([str(num) for num in range(0,9)])
a_to_z = ''.join([chr(char) for char in range(97,(97+26))])
A_to_Z = ''.join([chr(char) for char in range(65,(65+26))])
special_char = "$#@"
valid_passwords=[]
password_check_set = set(a_to_z+A_to_Z+zero_to_nine+special_char)
for password in password_list:
    if(len(password) >= 6 and len(password) <=12 and set(a_to_z).intersection(password) and set(A_to_Z).intersection(password) and set(zero_to_nine).intersection(password)and set(special_char).intersection(password)):
        valid_passwords.append(password)
print(','.join(valid_passwords))