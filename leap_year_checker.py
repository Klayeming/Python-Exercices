"""
Module: Leap Year Checker

Determines if a given year is a leap year or a regular year.

A year is a leap year if:
  - It is divisible by 4 AND not divisible by 100, OR
  - It is divisible by 400
"""

def year_bix(year):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        print(f"L'année {year} est bissextil")
    else:
        print(f"L'année {year} est civile")




year = int(input("Veuillez entre l'année à vérifier: "))
year_bix(year)