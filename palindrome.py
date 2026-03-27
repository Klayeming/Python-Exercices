"""
Module: Palindrome Checker

Determines if a text is a palindrome (reads the same forwards and backwards).
Ignores spaces and is case-insensitive.

Algorithm: Compare original (lowercased, no spaces) with reversed version.
"""

def est_palindrome(word):
    """Check if a word or phrase is a palindrome.
    
    Args:
        word (str): Input text to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    reverse_word = word[::-1]
    if word.lower().replace(" ","") == reverse_word.lower().replace(" ",""):
        return True

text = input("Veuillez saisir votre texte : ")
if est_palindrome(text):
    print(f"Le mot {text} est un palindrome")
else:
    print(f"Le mot {text} n'est pas un palindrome")