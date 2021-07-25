from model import joueurs
from vue import basic_functions, display_menus
import time
from tinydb import TinyDB

def save_players(saved_players, db_players):
    db_players.truncate()
    for player in saved_players:
        db_players.insert(player.serialize_player())

def create_player(saved_players, db_players):

    i = 0
    j = basic_functions.entry_user_int("Combien de joueurs voulez vous créer ? (1-20)\n", 1, 20)
    while i < j:
        new_player = joueurs.Joueurs(input("Prénom :\n"),
                                        input("Nom :\n"),
                                        input("Date de naissance (Format JJ/MM/AAA) :\n"), #format à vérifier
                                        input("Sexe (M/F) :\n"),
                                        0)

        saved_players.append(new_player)
        print("="*20)
        i += 1
    
    save_players(saved_players, db_players)

    return saved_players

    #     for joueur in saved_players:
    #         joueur.display()
        
    #     input()

    # if choix_utilisateur == 2:
    #     if len(saved_players) == 0:
    #         print("Pas de joueur enregistré, retour menu.")

    #     else:
    #         for joueur in saved_players:
    #             joueur.display()     

    # if choix_utilisateur == 3:
    #     if len(saved_players) == 0:
    #         print("Pas de joueur enregistré, retour menu.")
    #         time.sleep(2)

    #     for joueur in saved_players:
    #         joueur.display()       
    #         time.sleep(2)
    
    # display_menus.menu()