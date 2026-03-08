def salaire_base(heure_prest, taux_haoraire):
    return heure_prest * taux_haoraire

def salaire_brut(salaire_base, bonus = 0.5):
    return salaire_base + (bonus * salaire_base)

def salire_net(salaire_brut, impot = 0.05):
    return salaire_brut - (salaire_brut * impot)

heure_prest = int(input("Veuillez saisir les heures presté : "))
taux_haoraire = float(input("Veuillez saisir les taux horaire : "))

sal_base = salaire_base(heure_prest, taux_haoraire)
sal_brut = salaire_brut(sal_base)
sal_net = salire_net(sal_brut)

print(int(sal_net))

