# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:35:48 2022

@author: 14255
"""


import pandas as pd

nba_4q_stats_all = pd.read_csv("https://raw.githubusercontent.com/brianyoon4/project1_nba_q4_stats_csv/main/q4playerstatsall.csv")
#Benchmark 1: Loading data from a CSV file
print(" ")
print("Benchmark 1:")
print("Below is the original CSV file uploaded into a Pandas data frame")
print(nba_4q_stats_all)
print(" ")

nba_4q_stats_primary = pd.DataFrame(nba_4q_stats_all, columns=['Player', 'G', 'FG.', 'PTS', 
                                                           'TRB', 'AST', 'STL', 'BLK', 'TOV'])

nba_players = nba_4q_stats_all['Player']
nba_game_numbers = nba_4q_stats_all['G']
nba_4q_fgpct = nba_4q_stats_all['FG.']
nba_4q_ppg = round(nba_4q_stats_primary['PTS'] / nba_4q_stats_primary['G'], 1)
nba_4q_rpg = round(nba_4q_stats_primary['TRB'] / nba_4q_stats_primary['G'], 1)
nba_4q_apg = round(nba_4q_stats_primary['AST'] / nba_4q_stats_primary['G'], 1)
nba_4q_spg = round(nba_4q_stats_primary['STL'] / nba_4q_stats_primary['G'], 1)
nba_4q_bpg = round(nba_4q_stats_primary['BLK'] / nba_4q_stats_primary['G'], 1)
#Benchmark 3: All of these columns are new columns because the original data frame only lists
#these statistics as totals rather than per-game stats
pergame_data = {'Player': nba_players,
                'Games': nba_game_numbers,
                'FG PCT': nba_4q_fgpct,
                'PPG': nba_4q_ppg,
                'RPG': nba_4q_rpg,
                'APG': nba_4q_apg,
                'SPG': nba_4q_spg,
                'BPG': nba_4q_bpg}
nba_4q_pergame_stats = pd.DataFrame(pergame_data)

numofrows = len(nba_4q_pergame_stats.axes[0])
numofcols = len(nba_4q_pergame_stats.axes[1])
#Benchmark 5: This code above finds the number of rows and columns of the new data frame
#The data frame is indexed by players in the rows

print("Benchmark 3:")
print("I have added columns into a new data frame outlining the players' per-game stats in the 4th quarter")
print("This new data frame is shown below")
print(nba_4q_pergame_stats)
print(" ")
print("Benchmark 5:")
print("Number of qualifying players listed: ", numofrows)
print("Number of columns: ", numofcols)
