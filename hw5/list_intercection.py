def sameElement(a,b,c):
    for i in a:

        for j in b:
            if i == j:
                c.append(i)

    if len(c) == 0:
        c.append("None")

    return c

firstList=[1,2,3,"foo"]
secondList=[2,"foo",6,7]
c=[]
result = sameElement(firstList,secondList,c)
print(c)

def list_intercection(a, b):
    c = []
    for i in a:

        for j in b:
            if i == j:
                c.append(i)

    if len(c) == 0:
        c.append("None")

    return c

assert list_intercection([1, 1, 1, 2], [1, 3, 4]) == [1]#ваша функція не пройде цей тест
assert list_intercection(["foo", 1, "bar"], [2, 3, 4]) == None
assert list_intercection(["foo", 1, "bar"], []) == None
assert list_intercection(["foo", 1, "bar"], [4, "foo", 7]) == ["foo", ]