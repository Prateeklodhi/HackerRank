import datetime

while True:
    try:
        birth_day = int(input("Enter Birth year:"))
        break
    except ValueError:
        print("Invalid Input...")

current_date = datetime.date.today()
CURRENT_YEAR = int(str(current_date)[0:4])
age = CURRENT_YEAR-birth_day
print(f"Your age is: {age} years")
