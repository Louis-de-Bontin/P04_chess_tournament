from vue.basic_functions import entry_user_int, print_

def choix3(saved_tournaments, db_tournaments):
    i = 1
    for tournament in saved_tournaments:
        print_(str(i) +") Tournois : " + str(i))
        i += 1
        tournament.display_tournament()
    indice_tournament = entry_user_int("Quel tournoi voulez vous reprendre ?", 1, len(saved_tournaments)) - 1

    saved_tournaments[indice_tournament].display_tournament()
    saved_tournaments[indice_tournament].process_tournament(saved_tournaments, db_tournaments)