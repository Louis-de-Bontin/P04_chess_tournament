from model.tournaments import Tournaments
from vue import message, basic_functions
from vue.basic_functions import print_, entry_user_int

# Permet d'afficher les differents menus. Chaque méthode récupère le choix de l'utilisateur.
class Menus:
    
    def display_main_menu(self):
        print_(message.main_menu)
        choix_utilisateur = entry_user_int("Que voulez vous faire ?\n", 1, 5)
        return choix_utilisateur

    
    def display_tournament_menu(self):
        print_(message.tournament_menu)
        choix_utilisateur = entry_user_int("Que voulez vous faire ?\n", 4, 20, pair=True)
        return choix_utilisateur
    
    def display_player_menu(self):
        print_(message.player_menu)
        choix_utilisateur = basic_functions.entry_user_int("Que voulez vous faire ?\n", 1, 3)
        return choix_utilisateur

    def display_tournament_loading_menu(self, saved_tournaments, db_tournaments, saved_players, db_players):
        tournaments_playing = []
        for tournament in saved_tournaments:
            if tournament.status == "playing":
                tournaments_playing.append(tournament)

        if len(tournaments_playing) == 0:
            print_("Aucun tournois en cours.")
        else:
            print_(message.load_tournament_menu)
            i = 1
            for tournament in tournaments_playing:
                print_("\nEntrez la commande : (" +str(i) +") pour reprendre le tournois : " + tournament.name)
                i += 1
                tournament.display_tournament_basic()
            choix_utilisateur = entry_user_int("Quel tournoi voulez vous reprendre ?", 1, len(tournaments_playing)) - 1

            print_("Reprise du tournois suivant :")
            tournaments_playing[choix_utilisateur].display_tournament()
            tournaments_playing[choix_utilisateur].process_tournament(saved_tournaments, db_tournaments, saved_players, db_players)
    
    def display_tournament_results_menu(self, saved_tournaments):
        tournaments_over = []
        for tournament in saved_tournaments:
            if tournament.status == "Over":
                tournaments_over.append(tournament)

        i = 0
        for tournament in tournaments_over:
            if tournament.status == "Over":
                i+=1
                print_("Tournois : ", i)
                tournament.display_tournament_basic()
        choix_utilisateur = entry_user_int("Que voulez vous faire ?\n", 1, i)
        print_("\n\n\nVoici les résultats du tournois :")
        tournaments_over[choix_utilisateur - 1].display_tournament()