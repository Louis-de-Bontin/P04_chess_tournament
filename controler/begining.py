from controler.load_db import load_db
from controler.menu_principal import menu_principal


def begin_prog():
    data = load_db()
    saved_players = data[0]
    saved_tournaments = data[1]
    db_players = data[2]
    db_tournaments = data[3]

    menu_principal(saved_players, saved_tournaments, db_players, db_tournaments)
