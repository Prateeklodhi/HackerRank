# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(function):
    # code here
    def wrapper(*args,**kwargs):
        print(type(args),type(kwargs))
        if args[0]['valid']== True:
            return function(*args,**kwargs)
        else:
            print('Sorry,Your are not an Authenticated user!')
    return wrapper

@authenticated
def message_friends(user,value):
    print('message has been sent')

message_friends(user1)