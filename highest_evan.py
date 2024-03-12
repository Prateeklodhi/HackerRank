def highest_evan(num_list):
    prev_evan = 0
    for number in num_list:
        if (number % 2 == 0):
            if (number > prev_evan):
                prev_evan = number
    return prev_evan


print(highest_evan([2, 10, 32, 42, 23, 1]))
