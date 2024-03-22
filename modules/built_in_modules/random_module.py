'''
This file demonstrate the use of built in module name random and it's functions
'''
import random as ram

print(ram.random())# give a random value between 0,1
print(ram.randint(1,6))# gives a random integer between 1,6
print(ram.choice(['Prateek','Sunny','Leon']))# gives a random choice from a given iterable
names =['Prateek','Sunny','Leon']
ram.shuffle(names)# it suffles the given iterable randomly
print(names)
