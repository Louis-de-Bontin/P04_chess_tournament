def print_(*arg):
    for a in arg:
        print(a, end = '')
    print("","")

def entry_user_int(text, min, max, pair=False):
    while True:
        try:
            choix_utilisateur = int(input(text))
            if choix_utilisateur < min or choix_utilisateur > max:
                print("Mauvaise entrée, réessayer :")
                continue
            if pair and choix_utilisateur%2 != 0:
                print("Mauvaise entrée, réessayer :")
                continue
            break
        except:
            print("Mauvaise entrée, réessayer :")
            continue
    return choix_utilisateur

def multiple_user_entry(text, nb_entry, nb_saved_players):
    i = 0
    entry = []
    while len(entry) < nb_entry:
        entry.append(entry_user_int(text, 1, nb_saved_players)-1)
    return entry



def display_players_header():
    print(
        "|       Prénom       |" +
        "         Nom        |" +
        " Date de naissance  |" +
        "        Sex         |" +
        "        Rang        |"
    )
    print(
        "|" + "-"*20 +
        "|" + "-"*20 +
        "|" + "-"*20 +
        "|" + "-"*20 +
        "|" + "-"*20 +
        "|"
    )