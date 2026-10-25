sanat= ["omena", "tietokone", "auto", "matematiikka", "koira"]

määrä=0

for sana in sanat:
    if len(sana)>5:
        määrä+=1

print("Yli 5 kirjainta sisältäviä sanoja:", määrä)