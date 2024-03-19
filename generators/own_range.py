'''
This program is the demonstration of the custom range function, where it create a custom range named as My_range
and it will iterate through a range start and end.
'''
class MyRange():
    def __init__(self,start,end):
        print('Calling the constructor...')
        self.start = start
        self.end = end+1

    def __iter__(self):
        print('Calling the iterator...')
        return self
    
    def __next__(self):
        print('Calling the next...')
        if self.start < self.end:
            number = self.start
            self.start += 1
            return number
        raise StopIteration
    
list_of_number = MyRange(1,6)
for item in list_of_number:
    print(item)