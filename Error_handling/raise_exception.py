'''
In python while using the try except we can also raise our own exceptions using the raise keyword 
this program is the demostration of the Custom exception using the raise...
'''
toxic_girls = []
try:
    my_life = input('Enter your loved one name:')
    if my_life in toxic_girls:
        raise Exception("Bro, time hi nikal le..")
except Exception as problem:
    print(problem)
else:
    print('Chal ye thik hi..')
finally:
    print('chal thik hai bhai bye.')

