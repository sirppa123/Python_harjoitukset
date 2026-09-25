pienin=None
suurin=None

while True:
    syote=input("Anna luku (tyhjä lopettaa):")

    if syote == "":
        break

    luku=float(syote)

    if pienin is None or luku < pienin:
        pienin= luku

    if suurin is None or luku> suurin:
        suurin= luku

print("pienin:", pienin)
print("suurin:", suurin)