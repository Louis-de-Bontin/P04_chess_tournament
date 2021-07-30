from vue.basic_functions import entry_user_int, print_
from model import rounds
from datetime import date
from model.rounds import display_matchs
# from controler.menu_principal import menu_principal, saved_players, saved_tournaments, db_players, db_tournaments

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
                participant[0].__str__() +
                " "*(30 - len(participant[0].__str__())) +
                "|" +
                str(participant[1]) +
                " "*(30 - len(str(participant[1]))) +
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

    def process_tournament(self, saved_tournaments, db_tournaments):
        print(saved_tournaments)
        del_index = saved_tournaments.index(self)
        saved_tournaments.pop(del_index)
        print(saved_tournaments)
        while self.rounds_count < self.nb_rounds:
            print(saved_tournaments)
            enter_result = entry_user_int("1) Entrer les résultats\n2) Retour au menu principale", 1, 2)
            if enter_result == 1:
                for match in self.rounds[self.rounds_count - 1].matchs:
                    display_matchs(match)
                    gagne = int(input(
                        "Qui a gagné ?\n1) " +
                        match[0][0].__str__() + " ou 2) " +
                        match[1][0].__str__() + " ou 3) Ex aeco")
                    )

                    # J'actualise les scores
                    if gagne == 1:
                        match[0][1] += 1
                    elif gagne == 2:
                        match[1][1] += 1
                    elif gagne == 3:
                        match[0][1] += 0.5
                        match[1][1] += 0.5
                    display_matchs(match)
                self.display_tournament()

                # Actualise le tournois dans la list et le sauvegarde dans la bdd
                saved_tournaments.append(self)
                print(saved_tournaments)
                self.save_tournaments(saved_tournaments, db_tournaments)
                print("ok4")

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
                break

        self.status = "terminated"

    def new_round(self):
        pass

    def save_tournaments(self, saved_tournaments, db_tournaments):
        db_tournaments.truncate()
        for tournament in saved_tournaments:
            serialized_tournament = tournament.serialize_tournament()
            db_tournaments.insert(serialized_tournament)

    def serialize_tournament(self):
        participants_list = []
        for participant in self.participants:
            serialized_participant = participant[0].serialize_player()
            participants_list.append([serialized_participant, participant[1], participant[2]])
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
