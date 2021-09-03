#!/usr/bin/python3

def majuscule(phrase):
    """
    met la premiere lettre en majuscule si ce n'est pas le cas
    """
    return phrase.capitalize()

def test_majuscule():
    resultat = majuscule("seb")
    assert resultat == 'Seb'

test_majuscule()

#phrase  = input("Entre la phrase a mettre en majuscule : ")
# phrase = "ou est la majuscule ?"
# majuscule(phrase)