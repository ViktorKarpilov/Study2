from my_library import validation

numbers = validation.list_int_valid()
def Recursivly_sum(massive):
    if(len(massive)>1):
        return massive.pop() + Recursivly_sum(massive)
    else:
        return massive.pop()

def For_sum(massive):
    res = 0
    for i in massive:
        res +=i
    return res

def While_sum(massive):
    res = 0
    while(len(massive)>0):
        res += massive.pop()
    return res
print(Recursivly_sum(numbers))