sukupuoli=input("Mikä on sukupuolesi?")

hemoglobiiniarvo=int(input("Mikä on sinun hemoglobiiniarvo?"))

if sukupuoli=="nainen":
    if hemoglobiiniarvo>175:
        print("Hemoglobiiniarvo on korkea.")
    elif hemoglobiiniarvo<117:
        print("Hemoglobiiniarvo on alhainen.")
    elif 175>hemoglobiiniarvo>117:
        print("Hemoglobiiniarvo on normaali.")

if sukupuoli=="mies":
    if hemoglobiiniarvo>195:
        print("Hemoglobiiniarvo on korkea.")
    elif hemoglobiiniarvo<134:
        print("Hemoglobiiniarvo on alhainen.")
    else:
        print("Hemoglobiiniarvo on normaali")