def minTwo(x):
    x.sort()
    return x[1]

a = [68,54,77,31,65,23,43,567,6765,32,45]
minSecNumber = minTwo(a)
print(minSecNumber)

def second_smallest(array):
    array.sort()
    return array[1]

assert second_smallest([1, 1, 2, 2, 3]) == 2#Не процде такий тест
assert second_smallest([1, 2, 2, 3]) == 2
assert second_smallest([-1, 10, -2, 2]) == -1
