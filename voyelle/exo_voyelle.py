liste_voyelles = ["a", "e", "i", "o", "u", "y"]
liste_consonnes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

while lettre_utilisateur == '':
    lettre_utilisateur = input("Donnez une lettre et je vous dirai si c'est une voyelle : ")

match lettre_utilisateur:
    case x if x in liste_voyelles:
        print("C'est une voyelle.")
    case x if x in liste_consonnes:
        print("C'est une consonne.")
    case _:
        print("Ce n'est ni une voyelle ni une consonne.")
