def second_largest_element(x):
    x.sort()
    return x[-2]

marks=[44,33,55,66,77,88,99]
a = second_largest_element(marks)
print(a)
