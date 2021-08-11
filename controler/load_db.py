from tinydb import TinyDB
from model import joueurs, tournaments, rounds


def load_db():
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
            for player in saved_players:
                database_name = player.first_name + player.last_name
                in_game_firstname = participant[0]["first_name"]
                in_game_lastname = participant[0]["last_name"]
                in_game_name = in_game_firstname + in_game_lastname
                if database_name == in_game_name:
                    recovered_participants.append([
                        player,
                        participant[1],
                        participant[2]
                    ])

        recovered_tournament.participants = recovered_participants

        recovered_rounds = []
        for round in recovered_tournament.rounds:
            recovered_matchs = []
            for match in round["matchs"]:
                for player in saved_players:
                    database_name = player.first_name + player.last_name
                    p1_in_game_firstname = match[0][0][0]["first_name"]
                    p1_in_game_lastname = match[0][0][0]["last_name"]
                    p2_in_game_firstname = match[1][0][0]["first_name"]
                    p2_in_game_lastname = match[1][0][0]["last_name"]
                    p1_in_game = p1_in_game_firstname + p1_in_game_lastname
                    p2_in_game = p2_in_game_firstname + p2_in_game_lastname
                    if database_name == p1_in_game:
                        player1 = player
                    if database_name == p2_in_game:
                        player2 = player
                recovered_match = (
                    [[
                        player1,
                        match[0][0][1],
                        match[0][0][2]
                    ], match[0][1]],
                    [[
                        player2,
                        match[1][0][1],
                        match[1][0][2]
                    ], match[1][1]]
                )
                recovered_matchs.append(recovered_match)

            recovered_round = rounds.Rounds(
                round["name"],
                recovered_matchs,
                round["datetime_start"],
                round["datetime_end"]
            )
            recovered_rounds.append(recovered_round)
        recovered_tournament.rounds = recovered_rounds

        saved_tournaments.append(recovered_tournament)
    return saved_players, saved_tournaments, db_players, db_tournaments
