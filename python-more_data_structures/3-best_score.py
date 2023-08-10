#!/usr/bin/python3

# function that returns a key with the biggest integer value
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    Real_Score = 0
    Score_key = ""
    for key, value in a_dictionary.items():
        if value > Real_Score:
            Real_Score = value
            Score_key = key
    return Score_key