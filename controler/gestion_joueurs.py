from model import joueurs
from vue.basic_functions import entry_user_int, print_, entry_str


def save_players(saved_players, db_players):
    db_players.truncate()
    for player in saved_players:
        db_players.insert(player.serialize_player())


def create_player(saved_players, db_players):
    i = 0
    j = entry_user_int(
        "Combien de joueurs voulez vous créer ? (1-20)\n",
        1,
        20
    )
    while i < j:
        while True:
            first_name = entry_str("Prénom : ", '[a-zA-Z ]+$')
            last_name = entry_str("Nom de famille : ", '[a-zA-Z ]+$')
            birthdate = entry_str("Date de naissance (Format JJ-MM-AAAA) : ")
            sex = entry_str("Sexe (M/F) : ", '[a-zA-Z ]+$', 1)
            rank = entry_user_int("Rang : ", 0, 9999999999)
            new_player = joueurs.Joueurs(
                                            first_name,
                                            last_name,
                                            birthdate,
                                            sex,
                                            rank
                                        )

            validation_infos = entry_user_int(
                "Les infos sont_elles correctes ? Yes(1) / No(2)",
                1,
                2
            )
            if validation_infos == 1:
                saved_players.append(new_player)
                print_("="*20)
                i += 1
                break
            else:
                continue

    save_players(saved_players, db_players)

    return saved_players
