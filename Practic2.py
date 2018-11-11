my_list = [11,5,[4,3,[53,3]], 4]
print('Список:', my_list)
def While_sum(massive):
    res=0
    while(len(massive)>0):
        number = massive.pop()
        if(type(number)==list):
            res += While_sum(number)
        else:
            res+=number
    return res
print('while:', While_sum(my_list))

def Recursion_with_change(massive):
    if(len(massive)>0):
        if(type(massive[0])==list):
            massive[0] = Recursion_with_change(massive[0])
        return massive[0] + Recursion_with_change(massive[1:])
    return 0
my_list = [11,5,[4,3,[53,3]], 4]
print('recursion with change:', Recursion_with_change(my_list))

def Recursion_with_acum(massive,i=0):

    current = 0
    if(i==len(massive)):
        return 0
    if(type(massive[i])==list):
        current += Recursion_with_acum(massive[i])
    else:
        current += massive[i]

    return current + Recursion_with_acum(massive,i+1)
my_list = [11,5,[4,3,[53,3]], 4]
print('recursion with acumulation:', Recursion_with_acum(my_list))