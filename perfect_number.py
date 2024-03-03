# Find perfect number

x = int(input("Enter a number :"))
total = 0
for i in range(1,x):
    if x % i == 0:
        total = total + i

if total == x:
    print("perfect number")
else:
    print("not perfect number")

