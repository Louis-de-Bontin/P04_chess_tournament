from vue.basic_functions import entry_user_int, print_

def choix3(saved_tournament):
    i = 1
    for tournament in saved_tournament:
        print_("Tournois : " + str(i))
        i += 1
        tournament.display_tournament()
    indice_tournament = entry_user_int("Quel tournoi voulez vous reprendre ?", 1, len(saved_tournament)) - 1

    saved_tournament[indice_tournament].display_tournament()
    saved_tournament[indice_tournament].process_tournament()