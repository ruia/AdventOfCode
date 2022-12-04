# 1ST COLUMN opponent

# A - ROCK
# B - PAPER
# C - SCISSORS

# 2ND COLUMN PLAYER AND POINTS

# X - ROCK - 1
# Y - PAPER - 2
# Z - SCISSORS - 3

# 0 LOST - 3 DRAW - 6 WON


score_values = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "LOST": 0,
    "DRAW": 3,
    "WIN": 6
}

symbols = {
    "A": "X",
    "B": "Y",
    "C": "Z",
    "X": "A",
    "Y": "B",
    "Z": "C"
}

def return_match_score(player, opponent):
    score = 0
    if ((player == "Y") and (opponent == "B")) or ((player == "X") and (opponent == "A")) or ((player == "Z") and (opponent == "C")):
        score += score_values['DRAW'] 
    elif ((player == "X") and (opponent == "C")) or ((player == "Y") and (opponent == "A")) or ((player == "Z") and (opponent == "B")):
        score += score_values['WIN']
    else :
        score += score_values['LOST']
    
    score += score_values[player]
    return score

def return_score(result, opponent):
    score = 0
    if (result == "Y"):
        score += score_values['DRAW'] + score_values[symbols[opponent]]
    elif (result == "X"):
        score += score_values['LOST']
        if (opponent == "A"):
            score += score_values['Z']
        elif (opponent == "B"):
            score += score_values['X']
        else:
            score += score_values['Y']
    else:
        score += score_values['WIN']
        if (opponent == "A"):
            score += score_values['Y']
        elif (opponent == "B"):
            score += score_values['Z']
        else:
            score += score_values['X']
    return score
    
with open("input.txt") as f:
    total_score = 0
    total_score_fixed = 0
    for line in f:
        tmp = line.strip().split(" ")
        match_score = return_match_score(tmp[1], tmp[0])
        # print(match_score)

        match_score_fixed = return_score(tmp[1], tmp[0])
        # print(match_score_fixed)

        total_score += match_score
        total_score_fixed += match_score_fixed

    print(total_score)    
    print(total_score_fixed)    