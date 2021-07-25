from vue import display_menus
from controler import choix_joueurs, choix_creer_tournois, choix_display_tournament, choix_continue_tournament
from tinydb import TinyDB
from model import joueurs, tournaments, rounds

# Je vais chercher ma liste de joueurs dans ma bdd, et je les deserialize
db_players = TinyDB('db_players.json')
saved_players = []
serialized_players = db_players.all()

db_tournaments = TinyDB("db_tournament.json")
saved_tournaments = []
serialized_tounaments = db_tournaments.all()

for player in serialized_players:
    recovered_player = joueurs.Joueurs(
        player["first_name"],
        player["last_name"],
        player["birthdate"],
        player["sex"],
        player["rank"]
    )
    saved_players.append(recovered_player)

for tournament in serialized_tounaments:
    recovered_tournament = tournaments.Tournaments(
        tournament["name"],
        tournament["location"],
        tournament["date_start"],
        tournament["date_end"],
        tournament["rounds"],
        tournament["rounds_count"],
        tournament["participants"],
        tournament["clocktype"],
        tournament["description"],
        tournament["status"],
        tournament["nb_joueurs"],
        tournament["nb_rounds"]
    )

    recovered_participants = []
    for participant in recovered_tournament.participants:
        recoverd_participant = joueurs.Joueurs(
            participant["first_name"],
            participant["last_name"],
            participant["birthdate"],
            participant["sex"],
            participant["rank"]
        )
        recovered_participants.append(recoverd_participant)
    recovered_tournament.participants = recovered_participants

    recovered_rounds = []
    for round in recovered_tournament.rounds:
        recovered_round = rounds.Rounds(
            round["name"],
            round["matchs"],
            round["datetime_start"],
            round["datetime_end"]
        )
        recovered_rounds.append(recovered_round)
    recovered_tournament.rounds = recovered_rounds

    saved_tournaments.append(recovered_tournament)



while True:
    # Affichage du menu principale
    menu = display_menus.Menus()
    choix_utilisateur = menu.display_main_menu()  

    if choix_utilisateur == 1:
        choix_creer_tournois.choix1(menu, saved_players, saved_tournaments, db_tournaments)

    elif choix_utilisateur == 2:
        choix_joueurs.choix2(menu, saved_players, db_players)

    elif choix_utilisateur == 3:
        choix_continue_tournament.choix3(saved_tournaments)

    elif choix_utilisateur == 4:
        choix_display_tournament.choix4(menu, saved_tournaments)

    elif choix_utilisateur == 5:
        exit()
