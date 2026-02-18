import random as rd

def check_number(start, end, nb_user):
    answer = False
    nb_random = rd.randint(start, end)
    if nb_random == nb_user :
        answer = True
    return answer

#default Number Game
answer = False
n = 0
start = 1
end = 3

nb_user = 0

while not answer:
    n += 1
    nb_user = int(input(f"Veuillez devinez le nombre de la plage entre {start} et {end} : "))
    answer = check_number(start, end, nb_user)
    if answer :
        break

print(f"Felicitation vous avez trouvé le nombre qui est {nb_user} avec {n} essaie")