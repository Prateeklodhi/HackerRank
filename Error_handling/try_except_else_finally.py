'''
In the below code, there is a demostration of the try except else and finally.
tyr : the block where we write our business logic
except : the block where we will handle our exception that is generated by our business logic
else : when our try block is successfully executed and there is no exception then else block will be executed
finally : what ever the result is whether there is an exception or not at the completion of try except else, finally will definetly excecuted.
'''
try:
    number = int(input("Enter only a number:"))
    get_bug = int(input('Enter zero for a blast..:'))
    if not get_bug:
        number/get_bug
except ValueError as exp:
    print('Value Error:',exp)
except ZeroDivisionError as exp:
    print('Zero Division Error:',exp)
except Exception as exp:
    print('Other Error:',exp)
else:
    print('Hmmm.... nice you avoided the bug...')
finally:
    print('Now Thank you for the submissions...')