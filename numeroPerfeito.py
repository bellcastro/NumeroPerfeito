# -- coding: utf-8 --
def numeroPerfeito (num):
    somador = 0
    for i in range (1,num):
        if num%i == 0:
            somador = somador+i
            print(i)
            
    if somador == num:
        return True
    else:
        return False