from vue.basic_functions import print_, entry_user_int, display_players_header, multiple_user_entry
from model import tournaments, rounds
from datetime import datetime

def check_name_available(saved_tournaments, name):
    for tournament in saved_tournaments:
        if name == tournament.name:
            name = input("Nom déjà utilisé, donner un nom au tournois.")
            name = check_name_available(saved_tournaments, name)
        else:
            pass        
    return name

def check_if_not_number(variable):
    try:
        print("Variable :", variable)
        float_variable = float(variable)
        variable = input("Le lieu ne peut être un nombre, où se passe le tournois ?")
        check_if_not_number(variable)
    except:
        pass
    return variable

def check_if_player_play_twice(index_participants, saved_players, nb_joueurs):
    print_("\n")
    if len(set(index_participants)) < len(index_participants):
        index_participants = multiple_user_entry("Un même joueur ne peut pas être inscrit 2 fois, qui participent ? (" + str(nb_joueurs) + " réponses)", nb_joueurs, len(saved_players))
        index_participants = check_if_player_play_twice(index_participants, saved_players, nb_joueurs)
        return index_participants
    else:
        return index_participants

def choix1(menu, saved_players, saved_tournaments, db_tournaments, db_players):
    if len(saved_players) < 4:
        print_("Pas assez de joueur enrigistré pour faire un tournois")
    else:
        nb_joueurs = menu.display_tournament_menu()
        if len(saved_players) > 0:
            
            name = input("Donner un nom au tournois.")
            name = check_name_available(saved_tournaments, name)

            location = input("Où se passe le tournois ?")
            location = check_if_not_number(location)

            date_start = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            date_end = "unknown"

            list_rounds = []
            print("liste rounds", list_rounds)

            i = 1
            for player in saved_players:
                print_(str(i) + ") " + str(player))
                i+=1
            index_participants = multiple_user_entry("Qui participent ? (" + str(nb_joueurs) + " réponses)", nb_joueurs, len(saved_players))
            index_participants = check_if_player_play_twice(index_participants, saved_players, nb_joueurs)
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
                new_tournament.process_tournament(saved_tournaments, db_tournaments, saved_players, db_players)
            else:
                del new_tournament
                choix1(menu, saved_players, saved_tournaments, db_tournaments)

        else:
            print_("Pas de joueur à afficher")