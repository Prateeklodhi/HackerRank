def fibbo(number):
    numebr_one = 0
    number_two = 1
    for number in range(number):
        yield numebr_one
        numebr_one , number_two = number_two ,numebr_one + number_two, 

fibbo_object = fibbo(21)
for item in range(21):
    print(next(fibbo_object))