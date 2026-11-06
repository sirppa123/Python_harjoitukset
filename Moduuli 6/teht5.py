def karsi_parittomat(lista):
    parilliset=[]

    for luku in lista:
        if luku % 2==0:
            parilliset.append(luku)

    return parilliset


luvut=[1,2,3,4,5,6,7,8]

karsittu_lista=karsi_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista:", karsittu_lista)