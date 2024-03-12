n = int(input())
fibbo = 0
for item in range(n):
    sum = fibbo + item
    fibbo = item
    print("---")
    print(sum)