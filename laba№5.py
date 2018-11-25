import pygame
pygame.init()
"""11)  Задати деяке число n.Створити список з цілих чисел, число елементів якого не перевищує n.Необхідно: • сформувати новий список з відсутніх
 чисел.Наприклад, n = 10, список - (1, 2, 3, 6, 7), тоді результат(4, 5, 8, 9); • з 'єднати два списки і впорядкувати. """
from my_library import validation

End = False
def Do_uppload(n,sett):
    sett = set(sett)
    res = set()
    for i in range(n-1):
        res.add(i+1)
    return (res-sett)
while (not End):
    number_n = validation.int_valid()
    lst = validation.list_int_valid()
    upload = Do_uppload(number_n,lst)
    print(upload)
    lst.extend(list(upload))
    lst.sort()
    print(lst)

    if(input("Exit?(yes,no)")=="yes"):
        End = True
