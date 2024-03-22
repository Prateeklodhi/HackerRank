'''
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:

D 300
D 300
W 200
D 100
Then, the output should be:

500
'''
transaction_list = []
total_amount = 0
while True:
    transaction,amount = input('Enter Your transactions:').split(' ')
    if transaction =='C' or amount=='0':
        break
    else:
        if transaction == 'D':
            total_amount += int(amount)
        if transaction =='W':
            total_amount -= int(amount)
print(total_amount)