# import pprint.PrettyPrinter as pp
from type_charts import Weaknesses, Strengths


def combined_weakness(type1, type2):
    combined = {}
    for matchup in type1:
        combined[matchup] = type1[matchup] * type2[matchup]
    return combined


def average_weakness(pkmn_type):
    total = 0
    for matchup in pkmn_type:
        total += pkmn_type[matchup]
    return total/16

weaknesses = Weaknesses()
strengths = Strengths()
# types = ["nor", "fir", "wat", "ele", "gra", "ice", "fig", "poi", "gro",
#          "fly", "psy", "bug", "roc", "gho", "dra", "dar", "ste", "fai"]

# for pkmn_type in weaknesses.type_list:
#     if average_weakness(weaknesses.type_list[pkmn_type]) < 1.1:
#         print(pkmn_type)
#         print(average_weakness(weaknesses.type_list[pkmn_type]))
