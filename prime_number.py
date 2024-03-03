# Find the prime number

x = int(input("Enter a number :"))
for i in range(2,x):
    if x % i == 0:
        print(f"{x} not a prime number")
        break
else:
    print(f"{x} is a prime number !!!")