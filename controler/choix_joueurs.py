from vue.basic_functions import print_, entry_user_int, display_players_header
from controler import gestion_joueurs


def choix2(menu, saved_players, db_players):
    # Affichage du menu de gestion de joueurs
    reponse_utilisateur = menu.display_player_menu()
    if reponse_utilisateur == 1:
        # Création de joueurs & affichage de ces derniers
        saved_players = gestion_joueurs.create_player(
            saved_players,
            db_players
        )
        for player in saved_players:
            player.display()

    if reponse_utilisateur == 2:
        # Affichage des joueurs existant
        # (ou d'un message d'information si il n'en n'existe aucun),
        # et selection de l'utilisateur
        if len(saved_players) > 0:
            i = 0
            for player in saved_players:
                print_(
                    str(i+1) + ") " +
                    player.first_name +
                    " " +
                    player.last_name +
                    " : Rang " +
                    str(player.rank)
                )
                i += 1

            user_index = entry_user_int(
                "Quel joueur voulez vous modifier ?",
                1,
                i
            ) - 1
            print_(
                "Modifier : " +
                saved_players[user_index].first_name +
                " " +
                saved_players[user_index].last_name
            )
            # Modification du rang du joueur
            saved_players[user_index].modify_player()
            gestion_joueurs.save_players(saved_players, db_players)

        else:
            print_("Pas de joueur à modifier")
    if reponse_utilisateur == 3:
        # Affichage des joueurs existant
        # (ou d'un message d'information si il n'en n'existe aucun)
        display_players_header()
        if len(saved_players) > 0:
            for player in saved_players:
                player.display()
        else:
            print_("Pas de joueur à afficher")
