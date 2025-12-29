#Structure_conditionnelle_à_choix_multiple___if_..._elif_..._else_...

valeur = int(input("Entrez le nombre de photocopie a faire : "))
if valeur <= 10:
    facture = valeur * 0.30
    print(f"La facture est élevée à {facture} CDF.")
elif valeur <= 30:
    facture = 10 * 0.30 + (valeur - 10) * 0.25
    print(f"La facture est élevée à {facture} CDF.")
else:
    facture = 10 * 0.30 + 20 * 0.25 + (valeur - 30) * 0.20
    print(f"La facture est élevée à {facture} CDF.")