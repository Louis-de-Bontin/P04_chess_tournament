def print_(*arg):
    for a in arg:
        print(a, end = '')
    print("","")

def entry_user_int(text, min, max, pair=False, zero_autorized=True):
    while True:
        try:
            choix_utilisateur = int(input(text))
            if choix_utilisateur == 0 and zero_autorized:
                break
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

def multiple_user_entry(text, nb_entry):
    i = 0
    entry = []
    while i < nb_entry:
        i+=1
        entry.append(int(input(text))-1)
    return entry



def display_players_header():
    print("|       Prénom       |         Nom        | Date de naissance  |        Sex         |        Rang        |")
    print("|" + "-"*20 + "|" + "-"*20 + "|" + "-"*20 + "|" + "-"*20 + "|" + "-"*20 +"|")