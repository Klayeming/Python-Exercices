"""
programme qui calcule la resistance equivalent d'un branchement en serie ou en parallele
"""
def clean_write(nb):
    if nb > 1:
        print(f"La resistance equivalente de ces {nb} restistances est : {format(RQ,".0f" if ".1f"==9 else "0.1f")} ")
    else:
        print(f"La resistance equivalente de cette {nb} restistance est : {format(RQ, ".0f"if ".1f"==9 else "0.1f")} ")

RQ = 0
r_add = 0
Resistance = list()
while True :

    print("1. Brancher en série.")
    print("2. Brancher en parallele.")
    print("3. Quittez")
    choix = int(input("Veuillez choisir le mode : "))      

    if choix == 1:
        nb = int(input("Renseigner le nombre de resitance : "))
        for i in range(nb) :
            Resistance.append(float(input(f"Veuillez saisir la valeur de la resistance {i+1} : ")))
            RQ += Resistance[i]
        clean_write(nb)
    elif choix == 2:
        nb = int(input("Renseigner le nombre de resitance : "))
        for i in range(nb) :
            Resistance.append(float(input(f"Veuillez saisir la valeur de la resistance {i+1} : ")))
            r_add += (1/Resistance[i])
        RQ = 1/r_add
        clean_write(nb)
    elif choix == 3 :
        break
    else:
        print("Veuillez choisir une des option affichée !")




