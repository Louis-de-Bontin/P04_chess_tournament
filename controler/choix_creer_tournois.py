from vue.basic_functions import print_, entry_user_int, display_players_header, multiple_user_entry
from model import tournaments, rounds
from datetime import date

def choix1(menu, saved_players, saved_tournaments, db_tournaments):
    nb_joueurs = menu.display_tournament_menu()
    if len(saved_players) > 0:
        
        name = input("Donner un nom au tournois.")
        location = input("Ou se passe le tournois ?")
        date_start = date.today().strftime("%d/%m/%Y")
        date_end = "unknown"

        first_round = rounds.Rounds(
            "Round 1",
            [],
            date.today().strftime("%d/%m/%Y"),
            "unknown"            
        )
        list_rounds = [first_round]

        i = 1
        for player in saved_players:
            print_(str(i) + ") " + str(player))
            i+=1
        index_participants = multiple_user_entry("Qui participent ? (" + str(nb_joueurs) + " réponses)", nb_joueurs)
        participants = []
        for index in index_participants:
            # Mettre le score du tournois quelque part (class ?)
            new_player = saved_players[index]
            participants.append([new_player, 0, new_player.rank])
        
        clocktype_index = entry_user_int(
            "Quel est le type d'horloge ?" +
            "\n1) Bullet" +
            "\n2) Blitz" +
            "\n3) Tour rapide",
            1,
            3
        )
        if clocktype_index == 1:
            clocktype = "Bullet"
        if clocktype_index == 2:
            clocktype = "Blitz"
        if clocktype_index == 3:
            clocktype = "Tour rapide"

        description = input("Description : ")
        status = "playing"

        # list_rounds[0].create_match_first_round(participants)

        new_tournament = tournaments.Tournaments(
            name,
            location,
            date_start,
            date_end,
            list_rounds,
            1,
            participants,
            clocktype,
            description,
            status,
            nb_joueurs
        )

        new_tournament.display_tournament()
        validation_infos = entry_user_int("Les infos sont_elles correctes ? Yes(1) / No(2)", 1, 2)

        if validation_infos == 1:
            saved_tournaments.append(new_tournament)
            new_tournament.save_tournaments(saved_tournaments, db_tournaments)
            new_tournament.process_tournament(saved_tournaments, db_tournaments)
        else:
            del new_tournament
            choix1(menu, saved_players, saved_tournaments, db_tournaments)

    else:
        print_("Pas de joueur à afficher")