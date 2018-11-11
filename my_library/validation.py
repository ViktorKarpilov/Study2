
def int_valid():
    try:
        return int(input("Enter a number please : "))
    except:
        print("Someting wrong")
        return  int_valid()

def list_int_valid(massage = "write please list of numbers in format '1,2,3': "):
    try:
        res = []
        num=input(massage).split(",")
        for i in num:
            res.append(int(i))
        return res
    except:
        print("Something wrong")
        return list_int_valid()



