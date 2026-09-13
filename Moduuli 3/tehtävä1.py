pituus=int(input("Kuinka pitkä kuha on senttimetreinä? "))

if pituus<37:
    puuttuu=37-pituus
    print("Kuhan pituus on alamittainen, laita kuha takaisin järveen." f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu} cm.")
else:
    print("Kuhan pituus on riittävä.")
