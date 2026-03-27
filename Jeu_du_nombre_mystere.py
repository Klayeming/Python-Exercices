\"\"\"\nModule: Number Guessing Game

A simple guessing game where the player tries to guess a random number
between a given range. The game tracks the number of attempts.

Flow:
  1. Generate random number in range [start, end]
  2. Prompt user to guess
  3. Check if guess matches
  4. Display number of attempts used
\"\"\"

import random as rd

def check_number(start, end, nb_user):
    \"\"\"Check if user's guess matches the random number.
    
    Args:
        start (int): Minimum range value
        end (int): Maximum range value
        nb_user (int): User's guess
    
    Returns:
        bool: True if guess is correct, False otherwise
    \"\"\"
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