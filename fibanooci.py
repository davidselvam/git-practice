# Find the fibonacci series
# using for loop

x = int(input("Enter a number :"))
a,b = 0,1
for i in range(0,x):
    print(a)
    nth = a+b
    a = b
    b = nth
else:
    print("Execution completed")

# using while loop

n = int(input("Enter a number :"))
a,b = 0,1
count = 0
while count < n:
    print(a)
    nth = a+b
    a = b
    b = nth
    count +=1
else:
    print("Execution completed")
