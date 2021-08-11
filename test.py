# from tinydb import TinyDB
# from model import joueurs
# import operator
# # from model.round import Rounds
import re

# db_players = TinyDB('db_players.json')
# saved_players = []
# serialized_players = db_players.all()

# for player in serialized_players:
#     recovered_player = joueurs.Joueurs(
#         player["first_name"],
#         player["last_name"],
#         player["birthdate"],
#         player["sex"],
#         player["rank"]
#     )
#     saved_players.append(recovered_player)



# def create_match_first_round(players, matchs=None):
#     if not matchs:
#         # Je trie les joueurs en fonction de leur score (index 4 de la liste du joueur)
#         players.sort(key=operator.attrgetter('rank'))
#         # Je sépars la lise des joueurs en 2 listes (une avec la première moitier, et l'autre avec la 2eme moitier)
#         middle_index = len(players)//2
#         half1 = players[:middle_index]
#         half2 = players[middle_index:]

#         matchs = []
#         i = 0
#         # Tant que j'ai des joueurs dans une liste, je l'assotie avec le joueur avec le même classement dans l'autre moitier
#         while i < len(half1):
#             matchs.append(([half1[i].__str__(), 0], [half2[i].__str__(), 0]))
#             i += 1
    
#     # else:

#     return matchs

# # Je créé mes matchs et je les print
# matchs = create_match_first_round(saved_players)
# print(matchs)
# i = 1
# for match in matchs:
#     print("Match", i, ":", match[0][0], match[0][1], "VS", match[1][0], match[1][1])
#     i +=1

# while True:
#     # Je demande à l'utilisateur de terminer un match & d'entrer le vainqueur
#     end_match = int(input("Quel match voulez vous terminer ?"))
#     gagne = int(input(
#                     "Qui a gagné ?\n1) " +
#                     matchs[end_match-1][0][0] + " ou 2) " +
#                     matchs[end_match-1][1][0] + " ou 3) Ex aeco")
#                     )

#     # J'actualise les scores
#     if gagne == 1:
#         matchs[end_match-1][0][1] += 1
#     elif gagne == 2:
#         matchs[end_match-1][1][1] += 1
#     elif gagne == 3:
#         matchs[end_match-1][0][1] += 0.5
#         matchs[end_match-1][1][1] += 0.5
    
#     j=0
#     my_vars  = {}
#     compteur = 0
#     for j in range(len(matchs)):
#         var_name = "tot_score%d" % j
#         my_vars[var_name] = matchs[j][0][1] + matchs[j][1][1]
#         compteur = compteur + my_vars[var_name]
#         print(my_vars[var_name]) 
#     if compteur == len(matchs):
#         break

# # for match in matchs:
# #     print("Match", i, ":", match[0][0][0], match[0][0][1], "VS", match[1][0][0], match[1][0][1])
# #     i +=1
# print(matchs)
# a = ["a", "d"]
# for i in range(len(a)):
#     print(i)

a = "Salut /"
patern = '[a-zA-Z\s]+$'
match= bool(re.match(patern, a))
print(match)

# if len(match) > 0:
#     print("ok")