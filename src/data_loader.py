# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:01:49 2026

@author: Atefe
"""

import pandas as pd



def load_teams():
    # from csv file
    df = pd.read_csv("datafile.csv")
    df = df.dropna()
    return df

