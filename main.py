"""
Programme fait par Raul Mic
Groupe: 403
Description: TP1 : Compter le nombre des mots
"""

phrase = "Je suis une variable de type string qui sert a compter le nombre de mots pour TP1"

def count_word(p_phrase):
   """
   Cette fonction compte le nombre mots dans une phrase
       Paramètre:
       - p_phrase: la phrase pour compter le nombre de mots
   """
   return print(len(p_phrase.split(" ")))

print("Nombre de mots :")
print(count_word(phrase))
