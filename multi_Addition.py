p = 0
nb1 = int(input("saisir le nombre 1 : "))
nb2 = int(input("saisir le nombre 2 : "))
while nb1<0 or nb2<0 :
    print("veuillez saisir des entiers positives")
    nb1 = int(input("saisir le nombre 1 : "))
    nb2 = int(input("saisir le nombre 2 : ")) 
r = nb1*nb2
re = 0
"""while nb1 != 0 :
    p = p + nb2
    nb1 = nb1 - 1
nb1 = r"""
while re != r:
    re  += nb1
"""while p < nb2 :
    re += nb1 
    p += 1"""
#print("le produit de {} et {} par addition est {}" .format(nb1, nb2, re))
print(f"le produit de {nb1} et {nb2} par addition est {re}")