# Sample Input output
"""
$ python elo.py 2500 2200 24 2
---Player One---
Old Elo Rating: '2500'
New Elo Rating: 2478.181818181818
---Player Two---
Old Elo Rating: '2200'
New Elo Rating: 2212.0
"""

from sys import argv
from math import pow

def get_exp_score(rank1,rank2):
    exp= 1.0/(1.0 + pow(10, ((rank2-rank1)/400)))
    return exp

def modifyrating(current_rating, expected_score, final_score, k_factor):
    new_rating = current_rating + k_factor*(final_score - expected_score)
    return new_rating

def get_final_score(win_value):
    if win_value == 1:
        return (1, 0)
    elif win_value == 2:
        return (0, 1)
    elif win_value == 3:
        return(0.5, 0.5)
    else:
        return (0.5, 0.5)

def score_card(r_current, r_new):
    print "Old Elo Rating: %r" % r_current
    print "New Elo Rating: %r" % r_new

def main(args):
    if len(args)==5:
        _, r1_current, r2_current, k_factor, win_value = args
        Er1 = get_exp_score(int(r1_current), int(r2_current))
        Er2 = get_exp_score(int(r2_current), int(r1_current))
        (final_1, final_2) = get_final_score(int(win_value))
        r1_new = modifyrating(int(r1_current), Er1, final_1, int(k_factor))
        r2_new = modifyrating(int(r2_current), Er2, final_2, int(k_factor))
        print "---Player One---"
        score_card(r1_current, r1_new)
        print "---Player Two---"
        score_card(r2_current, r2_new)
    else:
        print("Args not given")

if __name__=="__main__":
    main(argv)