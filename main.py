# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:54:59 2026

@author: Atefe
"""
import sys
import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PROJECT_ROOT)


from src.data_loader import load_teams
from src.group_stage import run_group_stage, rank_teams, print_table




def main():
    teams = load_teams()
   
    points = run_group_stage(teams)
    
    ranking = rank_teams(points)
    
    print_table(ranking)
    
    print(ranking)
    
if __name__ == "__main__":
    main()


