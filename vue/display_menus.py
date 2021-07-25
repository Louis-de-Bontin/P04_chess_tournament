from vue import message, basic_functions
from vue.basic_functions import print_

# Permet d'afficher les differents menus. Chaque méthode récupère le choix de l'utilisateur.
class Menus:
    
    def display_main_menu(self):
        print_(message.main_menu)
        choix_utilisateur = basic_functions.entry_user_int("Que voulez vous faire ?\n", 1, 5)
        return choix_utilisateur

    
    def display_tournament_menu(self):
        print_(message.tournament_menu)
        choix_utilisateur = basic_functions.entry_user_int("Que voulez vous faire ?\n", 4, 20, pair=True)
        return choix_utilisateur
    
    def display_player_menu(self):
        print_(message.player_menu)
        choix_utilisateur = basic_functions.entry_user_int("Que voulez vous faire ?\n", 1, 3)
        return choix_utilisateur

    def display_tournament_loading_menu(self):
        print_(message.load_tournament_menu)
        choix_utilisateur = basic_functions.entry_user_int("Que voulez vous faire ?\n", 1, 5)
        return choix_utilisateur
    
    def display_tournament_results_menu(self, saved_tournaments):
        i = 0
        for tournament in saved_tournaments:
            i+=1
            basic_functions.print_("Tournois : ", i)
            tournament.display_tournament()
        choix_utilisateur = basic_functions.entry_user_int("Que voulez vous faire ?\n", 1, i)
        return choix_utilisateur
