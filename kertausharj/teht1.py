tuntipalkka=float(input("Anna tuntipalkka:"))
tunnit=float(input("Anna tehdyt tunnit:"))
päivä=input("Anna viikonpäivä:")

if päivä.lower() == "sunnuntai":
    palkka=tuntipalkka * 2 * tunnit
else:
    palkka=tuntipalkka * tunnit

print("Päiväpalkka", palkka, "€")

