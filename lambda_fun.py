# lambda function

x =  lambda x,y : x + y
print(x(4,4))

# map function
def addition(number):
     return number + number
number = [44,55,66,77]
x = map(addition,number)
print(list(x))

# lambda function
subtract = lambda x , y  : x - y
print(subtract(55,5))