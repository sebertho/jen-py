#!/usr/bin/python3

def majuscule(phrase):
    """
    met la premiere lettre en majuscule si ce n'est pas le cas
    """
    maj = phrase.capitalize()
    print(maj)

#phrase  = input("Entre la phrase a mettre en majuscule : ")
phrase = "ou est la majuscule ?"
majuscule(phrase)