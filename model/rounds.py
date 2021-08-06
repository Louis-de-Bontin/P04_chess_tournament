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

class Rounds:
    def __init__(self, name, matchs, datetime_start, datetime_end):
        self.name = name
        self.matchs = matchs
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end

    def create_match_first_round(self, players):
        numero_round = re.findall('[0-9]+', self.name)
        if numero_round[0] == 1 and len(numero_round) == 0:
            # Je trie les joueurs en fonction de leur score (index 4 de la liste du joueur)
            players.sort(key = lambda x: x[2])
        else:
            players.sort(key=lambda sl: (-sl[1],sl[2]))
        
        # Je sépars la lise des joueurs en 2 listes (une avec la première moitier, et l'autre avec la 2eme moitier)
        middle_index = len(players)//2
        half1 = players[:middle_index]
        half2 = players[middle_index:]

        matchs = []
        i = 0
        # Tant que j'ai des joueurs dans une liste, je l'assotie avec le joueur avec le même classement dans l'autre moitier
        while i < len(half1):
            matchs.append(([half1[i], 0], [half2[i], 0])) # Un match est un tuple
            i += 1
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
            print("saving", match)
            match_list.append(
                (
                    [[match[0][0][0].serialize_player(), match[0][0][1], match[0][0][2]], match[0][1]],
                    [[match[1][0][0].serialize_player(), match[1][0][1], match[1][0][2]], match[1][1]]
                )
            )
        serialized_round = {
            "name" : self.name,
            "matchs" : match_list,
            "datetime_start" : self.datetime_start,
            "datetime_end" : self.datetime_end
        }
        return serialized_round