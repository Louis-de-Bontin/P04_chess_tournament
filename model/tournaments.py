from vue.basic_functions import entry_user_int, print_
from model import rounds
from datetime import date

class Tournaments:
    def __init__(
        self,
        name,
        location,
        date_start,
        date_end,
        rounds,
        rounds_count,
        participants,
        clocktype,
        description,
        status,
        nb_joueurs = 4,
        nb_rounds = 4
    ):

        self.name = name
        self.location = location
        self.date_start = date_start
        self.date_end = date_end
        self.rounds = rounds
        self.rounds_count = rounds_count
        self.participants = participants
        self.clocktype = clocktype
        self.description = description
        self.status = status
        self.nb_joueurs = nb_joueurs
        self.nb_rounds = nb_rounds

    def display_tournament(self):
        print_(
            "|Infos --> Name : " +
            self.name +
            "; Lieu : " +
            self.location +
            "; Début : " +
            self.date_start +
            "; Fin : " +
            self.date_end +
            "; Round N°" +
            str(len(self.rounds)) +
            "; Clocktype : " +
            self.clocktype +
            "; Status :" +
            self.status +
            "|\n|Description : " +
            self.description +
            "|\n|Players :" +
            " "*21 + "|" +
            "Score :" +
            " "*23 + "|" +
            "\n|" + "-"*61 + "|"
        )
        for participant in self.participants:
            print_(
                "|" + 
                participant.__str__() +
                " "*(30 - len(participant.__str__())) +
                "|" +
                "*Score*" +
                " "*(30 - len("*Score*")) +
                "|"
            )
        print_("\n")

        for round in self.rounds:
            round.display_round()
        
        print_("\n\n")
    
    def modify_tournament(self):
        pass

    def end_tournament(self):
        pass

    def process_tournament(self):
        while self.rounds_count < self.nb_rounds:
            enter_result = entry_user_int("1) Entrer les résultats\n2) Retour au menu principale", 1, 2)
            if enter_result == 1:
                for match in self.rounds[self.rounds_count - 1].matchs:
                    print(match)
                    gagne = int(input(
                        "Qui a gagné ?\n1) " +
                        match[0][0] + " ou 2) " +
                        match[1][0] + " ou 3) Ex aeco")
                    )

                    # J'actualise les scores
                    if gagne == 1:
                        match[0][1] += 1
                    elif gagne == 2:
                        match[1][1] += 1
                    elif gagne == 3:
                        match[0][1] += 0.5
                        match[1][1] += 0.5
                    print(match, "\n")
                self.display_tournament()
                # SAUVEGARDER
                self.rounds_count += 1
                self.rounds.append(rounds.Rounds(
                    "Round " + str(self.rounds_count),
                    [],
                    date.today().strftime("%d/%m/%Y"),
                    "unknown"
                ))
                for round in self.rounds:
                    round.display_round()

            else:
                pass
        
        self.status = "terminated salut"

    def new_round(self):
        pass

    def serialize_tournament(self):
        participants_list = []
        for participant in self.participants:
            participants_list.append(participant.serialize_player())
        rounds_list = []
        for round in self.rounds:
            rounds_list.append(round.serialize_round())
        serialized_tournament = {
            "name" : self.name,
            "location" : self.location,
            "date_start" : self.date_start,
            "date_end" : self.date_end,
            "rounds" : rounds_list,
            "rounds_count" : self.rounds_count,
            "participants" : participants_list,
            "clocktype" : self.clocktype,
            "description" : self.description,
            "status" : self.status,
            "nb_joueurs" : self.nb_joueurs,
            "nb_rounds" : self.nb_rounds
        }
        return serialized_tournament
