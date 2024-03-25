import sys
import random
initial = int(sys.argv[1])
end = int(sys.argv[2])

guessing_number = random.randint(initial,end)
while True:
    try:
        guess = int(input("Guess the number :"))
        if guess==guessing_number:
            print("Woohooo! Right guess met...")
        elif guess > guessing_number:
            print("It's higher...")
            raise Exception('Opps! Wrong guess')
        else :
            print("It's lower...")
            raise Exception('Opps! Wrong guess')
    except ValueError:
        print("Only numbers are allowed...")
    except Exception as error:
        print(error)
    else:
        break