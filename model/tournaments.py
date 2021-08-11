from time import strftime
from vue.basic_functions import entry_user_int, print_
from model import rounds
from datetime import datetime
from model.rounds import display_matchs
from controler.gestion_joueurs import save_players


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
        nb_joueurs=4,
        nb_rounds=5
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

    def display_tournament_basic(self):
        print_(
            "Nom : " + self.name,
            "\nDescription : " + self.description,
            "\nRound " +
            str(self.rounds_count - 1) +
            "/" +
            str(self.nb_rounds - 1),
            "\nParticipants :"
        )
        for participant in self.participants:
            print_(participant[0].__str__())
        print_("\n")

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
            str(self.rounds_count) +
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
        self.participants.sort(key=lambda x: x[1], reverse=True)
        i = 1
        for participant in self.participants:
            print_(
                "|" + str(i) + ("->") +
                participant[0].__str__() +
                " "*(27 - len(participant[0].__str__())) +
                "|" +
                str(participant[1]) +
                " "*(30 - len(str(participant[1]))) +
                "|"
            )
            i += 1
        print_("\n")

        for round in self.rounds:
            round.display_round()

        print_("\n\n")

    def process_tournament(
        self,
        saved_tournaments,
        db_tournaments,
        saved_players,
        db_players
    ):
        if self.rounds_count == 1:
            round_default = entry_user_int(
                "Le nombre de rounds est de 4, continuer(1), changer(2) : ",
                1,
                2
            )
            if round_default == 2:
                self.nb_rounds = entry_user_int(
                    "Combien de rounds voulez vous faire ? (min 2, max : 20)",
                    2,
                    20
                ) + 1

        while self.rounds_count < self.nb_rounds:
            enter_result = entry_user_int(
                "1) Entrer les résultats\n2) Retour au menu principale",
                1,
                2
            )
            if enter_result == 1:
                del_index = saved_tournaments.index(self)
                saved_tournaments.pop(del_index)

                nb_matchs = 0
                tot_score_round = 0
                if self.rounds_count > 1:
                    for match in self.rounds[-1].matchs:
                        score_match = match[0][1] + match[1][1]
                        tot_score_round += score_match
                        nb_matchs += 1
                if tot_score_round == nb_matchs or nb_matchs == 0:
                    # Création d'un round
                    new_round = rounds.Rounds(
                        "Round " + str(self.rounds_count),
                        [],
                        datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                        "unknown"
                    )
                    # Création des matchs associés
                    new_round.create_match(self.participants, self.rounds)
                    self.rounds.append(new_round)

                for match in self.rounds[-1].matchs:
                    print_("Résultats :")
                    display_matchs(match)
                    gagne = entry_user_int(
                        "Qui a gagné ?\n1) " +
                        match[0][0][0].__str__() + " ou 2) " +
                        match[1][0][0].__str__() + " ou 3) Ex aeco",
                        1,
                        3
                    )

                    # J'actualise les scores
                    if gagne == 1:
                        match[0][1] += 1
                        match[0][0][1] += 1
                        match[0][0][2] += 1
                    elif gagne == 2:
                        match[1][1] += 1
                        match[1][0][1] += 1
                        match[1][0][2] += 1
                    elif gagne == 3:
                        match[0][1] += 0.5
                        match[0][0][1] += 0.5
                        match[0][0][2] += 0.5
                        match[1][1] += 0.5
                        match[1][0][1] += 0.5
                        match[1][0][2] += 0.5
                    display_matchs(match)

                now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                self.rounds[-1].datetime_end = now
                self.display_tournament()

                if self.rounds_count < self.nb_rounds:
                    self.rounds_count += 1

                # Actualise le tournois dans la list
                # et le sauvegarde dans la bdd et
                # actualise le rank des joueurs dans la bdd
                saved_tournaments.append(self)
                for player in self.participants:
                    saved_players.pop(saved_players.index(player[0]))
                    player[0].rank = player[2]
                    saved_players.append(player[0])

                save_players(saved_players, db_players)
                self.save_tournaments(saved_tournaments, db_tournaments)

                a = entry_user_int("Continuer ? (Oui/Non : 1/2)", 1, 2)
                if a == 2:
                    enter_result = 2
                    break

            else:
                break

        if self.rounds_count == self.nb_rounds:
            self.rounds_count -= 1
            del_index = saved_tournaments.index(self)
            saved_tournaments.pop(del_index)
            self.status = "Over"
            self.date_end = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            saved_tournaments.append(self)
            self.save_tournaments(saved_tournaments, db_tournaments)

    def save_tournaments(self, saved_tournaments, db_tournaments):
        db_tournaments.truncate()
        for tournament in saved_tournaments:
            serialized_tournament = tournament.serialize_tournament()
            db_tournaments.insert(serialized_tournament)

    def serialize_tournament(self):
        participants_list = []
        for participant in self.participants:
            serialized_participant = participant[0].serialize_player()
            participants_list.append(
                [
                    serialized_participant,
                    participant[1],
                    participant[2]
                ]
            )
        rounds_list = []
        for round in self.rounds:
            rounds_list.append(round.serialize_round())
        serialized_tournament = {
            "name": self.name,
            "location": self.location,
            "date_start": self.date_start,
            "date_end": self.date_end,
            "rounds": rounds_list,
            "rounds_count": self.rounds_count,
            "participants": participants_list,
            "clocktype": self.clocktype,
            "description": self.description,
            "status": self.status,
            "nb_joueurs": self.nb_joueurs,
            "nb_rounds": self.nb_rounds
        }
        return serialized_tournament
