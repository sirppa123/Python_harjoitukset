luvut=[]

while True:
    luku=int(input("Anna luku (0 lopettaa):"))

    if luku==0:
        break

    luvut.append(luku)

    print("Lisäysjärjestyksessä:", luvut)
    print("Järjesteltynä:", sorted(luvut))