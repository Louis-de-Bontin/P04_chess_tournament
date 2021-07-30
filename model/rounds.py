from vue.basic_functions import print_

def display_matchs(matchs):
    if isinstance(matchs, tuple):
        print_(
            matchs[0][0].__str__() +
            " VS " +
            matchs[1][0].__str__() +
            "(" +
            str(matchs[0][1]) +
            " - " +
            str(matchs[1][1]) +
            ")"
        )
    elif isinstance(matchs, list):
        for match in matchs:
            print_(
                match[0][0].__str__() +
                " VS " +
                match[1][0].__str__() +
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

    def modify_round(self):
        pass

    def end_round(self):
        pass

    def create_match_first_round(self, players, matchs=None):
        if not matchs:
            # Je trie les joueurs en fonction de leur score (index 4 de la liste du joueur)
            rank_player = players[0]
            players.sort(key = lambda x: x[2])
            # Je sépars la lise des joueurs en 2 listes (une avec la première moitier, et l'autre avec la 2eme moitier)
            middle_index = len(players)//2
            half1 = players[:middle_index]
            half2 = players[middle_index:]

            matchs = []
            i = 0
            # Tant que j'ai des joueurs dans une liste, je l'assotie avec le joueur avec le même classement dans l'autre moitier
            while i < len(half1):
                matchs.append((half1[i], half2[i])) # Un match est un tuple
                i += 1
        print(type(matchs))
        self.matchs = matchs
        display_matchs(matchs)
        
        # else:
        #     pass

    def display_current_matchs(self):
        pass

    def enter_match_results(self, match):
        pass

    def display_round(self):
        print_(
            "Round :" +
            self.name +
            "\nDébut :" +
            self.datetime_start +
            "\nMatchs :"
        )
        display_matchs(self.matchs)

    def serialize_round(self):
        match_list = []
        for match in self.matchs:
            match_list.append(([match[0][0].serialize_player(), match[0][1], match[0][2]], [match[1][0].serialize_player(), match[1][1], match[1][2]]))
        serialized_round = {
            "name" : self.name,
            "matchs" : match_list,
            "datetime_start" : self.datetime_start,
            "datetime_end" : self.datetime_end
        }
        return serialized_round