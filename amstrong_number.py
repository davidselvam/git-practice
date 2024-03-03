# Find Armstrong number

x =int(input("Enter a number :"))
str_x=str(x)
len_str_x=len(str_x)
total = 0
for i in str_x:
    total = total + int(i)**(len_str_x)
if x == total:
    print(f"{x} is a armstrong number !!")
else:
    print(f"{x} is not a armstrong number !!")
