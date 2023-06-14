#!/usr/bin/python3
def best_score(a_dictionary):

    highest_score = 0
    if not a_dictionary:
        return None
    for i in a_dictionary.keys():
        if highest_score < a_dictionary[i]:
            highest_score = a_dictionary[i]
    return highest_score


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
