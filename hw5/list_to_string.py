def fullWordFromList(x):
    full = ''.join(x)
    return full

leters = ["L", "i", "s", "t","i","k"]
result=fullWordFromList(leters)
print(result)


def fullWordInt(x):
    fullWord = ''.join([str(int) for int in x])
    return fullWord

newList= ["L", "i", "s", "t","i","k",2,1,2,3]
result=fullWordInt(newList)
print(result)

def list_to_string(array):
    fullWord = ''.join([str(int) for int in array])
    return fullWord

assert list_to_string(["l", "i", "s", "t"]) == "list"
assert list_to_string(["l", "i", "s", "t", 5, 1.1]) == "list51.1"