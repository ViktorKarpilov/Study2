from my_library import validation
numbers = validation.list_int_valid()
def Sum(massive):
    if(len(massive)>1):
        return massive.pop() + Sum(massive)
    else:
        return massive.pop()
print(Sum(numbers))