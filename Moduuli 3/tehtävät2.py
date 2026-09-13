hyttiluokka=input("Mikä on teidän hyttiluokka laivassa?").lower()

if hyttiluokka =="lux":
    print("Hyttiluokkanne on LUX, Lux on parvekkeellinen hytti yläkannella.")

elif hyttiluokka=="a":
    print("Hyttiluokkanne on A, A on ikkunallinen hytti autokannenn yläpuolella.")

elif hyttiluokka=="b":
    print("Hyttiluokkanne on B, B on ikkunaton hytti autokannen yläpuolella.")

elif hyttiluokka=="c":
    print("Hyttiluokkanne on C or c, C on ikkunaton hytti autokannen alapuolella.")

else: print("Valitettavasti en löytänyt hyttiluokkaanne, kokeile uudelleen.")