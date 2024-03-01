# Find the second largest element in the list

def second_largest_element(x):
    x.sort()
    return x[-2]

marks=[446,334,55,666,77,88,99]
a = second_largest_element(marks)
print(a)
