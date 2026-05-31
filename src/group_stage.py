# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:29:41 2026

@author: Atefe
"""

from src.match_simulator import simulate_match
from src.data_loader import load_teams


teams = load_teams()
def run_group_stage(teams):
    #Each team plays against every other team once.
    #Win = 3 points
    
    points = {team["name"]: 0 for team in teams.to_dict("records")}

    team_list = teams.to_dict("records")
    
    for i in range(len(team_list)):
        for j in range(i + 1, len(team_list)):
            winner = simulate_match (team_list [i], team_list [j])
            points[winner] += 3
    return points

points = run_group_stage(teams)
def rank_teams(points):
    return sorted(points.items(), key = lambda x: x[1] , reverse = True)


def print_table(ranking):
    print("\nFINAL STANDINGS\n")
    for i ,(team, pts) in enumerate(ranking, 1):
        print (f"{i}.{team} - {pts} pts")
       
