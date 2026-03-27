"""
Module: Time Converter (Seconds to Hours:Minutes:Seconds)

Converts a time duration given in seconds into hours, minutes, and seconds format.

Formulas:
  - Hours: total_seconds // 3600
  - Remaining: total_seconds % 3600
  - Minutes: remaining // 60
  - Seconds: remaining % 60
"""

Time = int(input("Veuillez ecrire le temps en secondes : "))
hour    = Time // 3600
minute  = (Time % 3600)// 60
seconde = (Time % 3600)%  60
print(f"voici le temps {Time} sec = {hour}h {minute}m {seconde}s")
