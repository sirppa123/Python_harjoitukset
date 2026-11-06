import math

def yksikköhinta(halkaisija, hinta):

    säde=halkaisija/2
    pinta_ala=math.pi*säde**2
    pinta_ala_m2=pinta_ala/10000

    yksikköhinta=hinta/pinta_ala_m2

    return yksikköhinta

halkaisija1=float(input("Anna ensimmäisen pizzan halkaisija (cm):"))
hinta1=float(input("Anna ensimmäisen pizzan hinta (€):"))

halkaisija2=float(input("Anna toisen pizzan halkaisija (cm):"))
hinta2=float(input("Anna toisen pizzan hinta (€):"))

yh1=yksikköhinta(halkaisija1, hinta1)
yh2=yksikköhinta(halkaisija2, hinta2)

if yh1<yh2:
    print("Ensimmäinen pizza antaa paremman vastinnen rahalle.")
else:
    print("Toinen pizza antaa paremman vastineen rahalle.")