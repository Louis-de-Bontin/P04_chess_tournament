import operator
from vue.basic_functions import print_

class Rounds:
    def __init__(self, name, matchs, datetime_start, datetime_end):
        self.name = name
        self.matchs = matchs
        self.datetime_start = datetime_start
        self.datetime_end = datetime_end
    
    def dispaly_round(self):
        pass

    def modify_round(self):
        pass

    def end_round(self):
        pass

    def create_match_first_round(self, players, matchs=None):
        if not matchs:
            # Je trie les joueurs en fonction de leur score (index 4 de la liste du joueur)
            players.sort(key=operator.attrgetter('rank'))
            # Je sépars la lise des joueurs en 2 listes (une avec la première moitier, et l'autre avec la 2eme moitier)
            middle_index = len(players)//2
            half1 = players[:middle_index]
            half2 = players[middle_index:]

            matchs = []
            i = 0
            # Tant que j'ai des joueurs dans une liste, je l'assotie avec le joueur avec le même classement dans l'autre moitier
            while i < len(half1):
                matchs.append(([half1[i].__str__(), 0], [half2[i].__str__(), 0]))
                i += 1
        
        self.matchs = matchs
        print_(matchs)
        
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
        for match in self.matchs:
            print_(match)

    def serialize_round(self):
        serialized_round = {
            "name" : self.name,
            "matchs" : self.matchs,
            "datetime_start" : self.datetime_start,
            "datetime_end" : self.datetime_end
        }
        return serialized_round