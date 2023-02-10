def plus(t):
    x = [3, 4, 5, 6, 7, 8, 8]
    string = ''
    for each in t:
        string += str(each)
    x = int(string)
    return x

b= [3,2,5,4,5,87,43,4,5,6,78]
v= plus(b)
print(v)
"""
Із списку, цілі числа з'єднати в одне число
варіант із зірочкою - заборонено переведення із строкового в числовий тип і навпаки
"""

def join_ints(t):
    string = ''
    for each in t:
        string += str(each)
    x = int(string)
    return x

assert join_ints([1, 2, 3]) == 123
assert join_ints([1, "foo", 2.5, 1, 1, 4, "abr", 3]) == 11143#Ваша функція не пройде цей тест
