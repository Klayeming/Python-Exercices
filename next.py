"""
#25 Ecrire un programme qui affiche le 10 prochain nombre apres celui saisie
"""
#La foctin range peut aussi prendre le parametre suivant pour faire la même chose
#range(<valeur de depart>,<valeur final+1>,<pas>)
#range(<nbr>) fait de 0->nbr-1
#range(<n>,<m>)fait de n->m-1
def tenNext(nbr):
    for i in range(10):
        nbr += 1
        print(f"{nbr}")
def tenNextv1_1(nbr):
    for i in range(nbr+1, nbr+11, 1):
        print(i)
def forrange(nbr, nbr2):
    for i in range(nbr, nbr2):
        print(i)

def tenNextV2_0(nbr):
    i = nbr +1
    while i <= (nbr+10):   
        print(f"{i}")
        i = i + 1

#nbr = int(input("Veuillez entre votre nombre: "))
#nbr2 = int(input("Veuillez entre votre nombre: "))
#tenNext(nbr)
#tenNextv1_1(nbr)
#forrange(nbr, nbr2)
#tenNextV2_0(nbr)

