from vue import display_menus
from controler import choix_joueurs, choix_creer_tournois, choix_display_tournament, choix_continue_tournament
# from controler.load_db import saved_players, saved_tournaments, db_players, db_tournaments

def menu_principal(saved_players, saved_tournaments, db_players, db_tournaments):
    while True:
        # Affichage du menu principale
        menu = display_menus.Menus()
        choix_utilisateur = menu.display_main_menu()  

        if choix_utilisateur == 1:
            choix_creer_tournois.choix1(menu, saved_players, saved_tournaments, db_tournaments)

        elif choix_utilisateur == 2:
            choix_joueurs.choix2(menu, saved_players, db_players)

        elif choix_utilisateur == 3:
            choix_continue_tournament.choix3(saved_tournaments, db_tournaments)

        elif choix_utilisateur == 4:
            choix_display_tournament.choix4(menu, saved_tournaments)

        elif choix_utilisateur == 5:
            exit()
