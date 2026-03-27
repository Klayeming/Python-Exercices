"""
Module: Photocopying Invoice Calculator

Calculates the cost of photocopies with tiered pricing:
  - 1-10 copies: 0.30 CDF each
  - 11-30 copies: 0.25 CDF each (after first 10)
  - 31+ copies: 0.20 CDF each (after first 30)
"""

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