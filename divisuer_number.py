"""
Docstring for divisuer_number
#31 Xrite a program who print divisor of postif number 
"""
def divisor_nub(nbr):
    for i in range(1, nbr+1):
        if nbr%i == 0:
            print(f"Les diviseurs de {nbr} sont :" if nbr>1 else "Le diviseur de 1 est :")
            print(i)
nbr = int(input("Please Write a number: "))
while nbr<=0:    
    nbr = int(input("Please Write a positif number: "))
divisor_nub(nbr)