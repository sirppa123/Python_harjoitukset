import random

def heitä_noppaa():
    return random.randint(1,6)

heitto=0

while heitto !=6:
    heitto=heitä_noppaa()
    print(heitto)

