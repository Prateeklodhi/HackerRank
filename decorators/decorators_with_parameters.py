'''
below code demostrates the use of function that has some perameters and pass them into the decorator...
'''
def my_deco(function):
    def wrapper(*args,**kwargs):
        function(*args,**kwargs)
    return wrapper

@my_deco
def hello(*args,**kwargs):
    print(f"Postional Agrguments: {''.join([item for item in args])}")
    keyword_arguments = kwargs
    print(keyword_arguments)
   
hello("Hi"," prateek"," I"," know"," you"," are"," going"," with"," lot's"," of"," problem"," but"," don't"," worry"," These"," problem"," will"," be"," there"," for"," sometime",' I'," am"," there"," for"," you"," always"," I", "am"," the"," inner"," you"," that"," won't"," let"," you go down...",my_name="inner you",love_for_you="100%",my_wish="To see you happy from your life")
