#!/usr/bin/python3
def best_score(a_dictionary):

    highest_score = 0
    if a_dictionary:
        for i in a_dictionary.keys():
            if highest_score < a_dictionary[i]:
                highest_score = a_dictionary[i]
    return highest_score
