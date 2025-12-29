#Programme_qui_change_contenus_de_deux_variables_selon_une_condition
A = int(input("Veuillez saisir la valeur du prémier nombre: "))
B = int(input("Veuillez saisir la valeur du deuxième nombre: "))

if A*B>0:
    C = A
    A = B
    B = C
    print(f"voici la valeur {A} ainsi que la deuxième valeur {B}")


else:
    C = A+B
    D = A*B
    A = C
    B = D
    print(f"voici la valeur {A} ainsi que la deuxième valeur {B}")
