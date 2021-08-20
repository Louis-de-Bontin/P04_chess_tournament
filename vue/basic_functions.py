import re
import datetime


def print_(*arg):
    for a in arg:
        print(a, end='')
    print("", "")


def entry_str(text, regex=None, length=20):
    while True:
        try:
            data = str(input(text))
            if regex:
                match = bool(re.match(regex, data))
                if match is False:
                    print("Mauvaise entrée, réessayer :")
                    continue
                if len(data) > length:
                    print("Nom trop long, réessayer :")
                    continue
                if length == 1 and (data != "M" and data != "F"):
                    print("Mauvaise entrée, réessayer :")
                    continue
            else:
                try:
                    datetime.datetime.strptime(data, '%d-%m-%Y')
                except ValueError:
                    print("Mauvais format de date (JJ-MM-AAAA) : ")
                    continue
            break
        except ValueError:
            print("Mauvaise entrée, réessayer :")
            continue
    return data


def entry_user_int(text, min, max, pair=False):
    while True:
        try:
            choix_utilisateur = int(input(text + "\n"))
            if choix_utilisateur < min or choix_utilisateur > max:
                print("Mauvaise entrée, réessayer :")
                continue
            if pair and choix_utilisateur % 2 != 0:
                print("Mauvaise entrée, réessayer :")
                continue
            break
        except ValueError:
            print("Mauvaise entrée, réessayer :")
            continue
    return choix_utilisateur


def multiple_user_entry(text, nb_entry, nb_saved_players):
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
