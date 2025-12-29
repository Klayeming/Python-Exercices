"""
Ecrire un programme qui demande un tepms(entier) exprimé en secondes, 
et qui le convertit en heures, minutes, secondes
"""
Time    = int(input("Veuillez ecrire le temps en secondes : "))
hour    = Time // 3600
minute  = (Time % 3600)// 60
seconde = (Time % 3600)%  60
print(f"voici le temps {Time} sec = {hour}h {minute}m {seconde}s")
