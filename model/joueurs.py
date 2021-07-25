from vue.basic_functions import entry_user_int, print_

class Joueurs:
    """
    Joueur :
-Nom de famille (str)
-Prénom (str)
-Date de naissance (datetime)
-Sexe (booléen)
-Classement (int)

-Être créé
-Être affiché
-Être modifié
-Modifier le classement
"""
    def __init__(self, first_name, last_name, birthdate, sex, rank):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.sex = sex
        self.rank = rank
    
    def display(self):
        print_(
            "|" + self.first_name + " "*(20-len(self.first_name)), 
            "|" + self.last_name + " "*(20-len(self.last_name)), 
            "|" + self.birthdate + " "*(20-len(self.birthdate)),
            "|" + self.sex + " "*(20-len(self.sex)),
            "|" + str(self.rank) + " "*(20-len(str(self.rank))),
            "|"
        )

    def modify_player(self):
        self.rank = int(input("Nouveau rang du joueur ?"))
        pass

    def serialize_player(self):
        serialized_player = {
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "birthdate" : self.birthdate,
            "sex" : self.sex,
            "rank" : self.rank
        }
        return serialized_player

    def __str__(self):
        nom_entier = self.first_name + " " + self.last_name
        return nom_entier
