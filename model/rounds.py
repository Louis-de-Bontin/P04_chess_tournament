from vue.basic_functions import print_
import re


def display_matchs(matchs):
    if isinstance(matchs, tuple):
        print_(
            matchs[0][0][0].__str__() +
            " VS " +
            matchs[1][0][0].__str__() +
            "(" +
            str(matchs[0][1]) +
            " - " +
            str(matchs[1][1]) +
            ")"
        )
    elif isinstance(matchs, list):
        for match in matchs:
            print_(
                match[0][0][0].__str__() +
                " VS " +
                match[1][0][0].__str__() +
                "(" +
                str(match[0][1]) +
                " - " +
                str(match[1][1]) +
                ")"
            )
    else:
        print_(type(matchs))


def check_if_already_played_together(match, matchs_played):
    match_to_check = (match[0][0][0], match[1][0][0])
    matchs_to_compare = []
    already_played = False
    for match in matchs_played:
        matchs_to_compare.append((match[0][0][0], match[1][0][0]))
    for match in matchs_to_compare:
        if (
            match_to_check[0] == match[0] and
            match_to_check[1] == match[1]
        ) or (
            match_to_check[1] == match[0] and
            match_to_check[0] == match[1]
        ):
            already_played = True
    return already_played


class Rounds:
    def __init__(self, name, matchs, datetime_start, datetime_end):
        self.name = name
        self.matchs = matchs
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end

    def create_match(self, players, rounds):
        numero_round_brut = re.findall('[0-9]+', self.name)
        numero_round = ""
        for numero in numero_round_brut:
            numero_round = numero_round + numero
        numero_round = int(numero_round)
        if numero_round == 1:
            # Je trie les joueurs en fonction de leur score
            # (index 4 de la liste du joueur)
            players.sort(key=lambda x: x[2])
        else:
            players.sort(key=lambda sl: (-sl[1], sl[2]))

        # Je sépars la lise des joueurs en 2 listes
        # (une avec la première moitier, et l'autre avec la 2eme moitier)
        middle_index = len(players)//2
        half1 = players[:middle_index]
        half2 = players[middle_index:]

        # Je regarde quels matchs ont déjà été joués
        matchs_played = []
        for round in rounds:
            for match_played in round.matchs:
                matchs_played.append(match_played)

        matchs = []
        # Petit algo pour associer des joueurs qui n'ont pas envore
        # jouer ensemble dans la mesure du possible
        # Pour chaque élément de la 1ere moitier,
        # je l'associe au premier joueur restant
        # dans la 2eme liste n'ayant pas jouer avec.
        # A défaut, le dernier joueur de la liste 2
        for i in range(len(half1)):
            a = True
            j = 0
            while a is True:
                j1 = half1[i]
                j2 = half2[j]
                match = ([j1, 0], [j2, 0])
                already_played = check_if_already_played_together(
                    match,
                    matchs_played
                )
                if already_played is True and j < len(half2)-1:
                    j += 1
                else:
                    matchs.append(match)
                    half2.pop(j)
                    a = False

        self.matchs = matchs

        print_("Nouveaux matchs :")
        display_matchs(matchs)
        print_("\n\n")

    def display_round(self):
        print_(
            "Round : " +
            self.name +
            "\nDébut : " +
            self.datetime_start +
            "\nFin : " +
            self.datetime_end +
            "\nMatchs : "
        )
        display_matchs(self.matchs)

    def serialize_round(self):
        match_list = []
        for match in self.matchs:
            match_list.append(
                (
                    [
                        [
                            match[0][0][0].serialize_player(),
                            match[0][0][1],
                            match[0][0][2]
                        ],
                        match[0][1]
                        ],
                    [
                        [
                            match[1][0][0].serialize_player(),
                            match[1][0][1],
                            match[1][0][2]
                        ],
                        match[1][1]
                    ]
                )
            )
        serialized_round = {
            "name": self.name,
            "matchs": match_list,
            "datetime_start": self.datetime_start,
            "datetime_end": self.datetime_end
        }
        return serialized_round
