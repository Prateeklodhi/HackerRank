# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
val = input()
new_list = []
for item in range(t):
    new_list.append(int(val.split(' ')[item].strip()))
print(new_list)
print(hash(tuple(new_list)))
t = (1, 2)
print(hash(t))