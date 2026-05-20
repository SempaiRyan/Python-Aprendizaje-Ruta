def sumar(*args):
    res=0

    #Iteramos cada elemento
    for valor in args:
        res+=valor
    return res
print(sumar(1,2,3,4,5,6,7,8,9))