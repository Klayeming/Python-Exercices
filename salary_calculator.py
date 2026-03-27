"""
Module: Salary Calculator with Bonus and Tax

Calculates net salary based on:
  1. Hourly rate × hours worked = base salary
  2. Add bonus (default 50% of base)
  3. Subtract tax (default 5%)

Formulas:
  Base = hours × hourly_rate
  Gross = Base × (1 + bonus)
  Net = Gross × (1 - tax)
"""

def salaire_base(heure_prest, taux_haoraire):
    """Calculate base salary."""
    return heure_prest * taux_haoraire

def salaire_brut(salaire_base, bonus=0.5):
    """Calculate gross salary with bonus."""
    return salaire_base + (bonus * salaire_base)

def salire_net(salaire_brut, impot=0.05):
    """Calculate net salary after tax deduction."""
    return salaire_brut - (salaire_brut * impot)

heure_prest = int(input("Veuillez saisir les heures presté : "))
taux_haoraire = float(input("Veuillez saisir les taux horaire : "))

sal_base = salaire_base(heure_prest, taux_haoraire)
sal_brut = salaire_brut(sal_base)
sal_net = salire_net(sal_brut)

print(f"Salaire net: {int(sal_net)} CDF")

