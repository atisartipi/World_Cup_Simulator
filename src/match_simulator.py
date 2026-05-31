# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:50:02 2026

@author: Atefe
"""

import random
#from data_loader import load_teams



def calculate_strength(teams):
    rank_score = 100 - teams["fifa_rank"]
    attack_score = teams["avg_goals_scored"] * 20
    defense_score = (3 - teams["avg_goals_conceded"]) * 15
    return rank_score + attack_score + defense_score


def simulate_match(team_a , team_b):
    strength_a = calculate_strength(team_a)
    strength_b = calculate_strength(team_b)
    
    prob_a = strength_a / (strength_a + strength_b)
    if random.random() < prob_a:
        return team_a["name"]
    else:
        return team_b["name"]
    
#teams = load_teams()
#iran = teams[teams["name"] == "Iran"].iloc[0]
#d = calculate_strength(iran)
#print(d))