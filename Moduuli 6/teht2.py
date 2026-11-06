import random

def heitä_noppaa(tahkot):
    return random.randint(1,tahkot)

maksimi=int(input("Anna nopan tahkojen määrä:"))

heitto=0

while heitto !=maksimi:
    heitto=heitä_noppaa(maksimi)
    print(heitto)
    