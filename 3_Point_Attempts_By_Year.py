# Basic BabyName analysis - Imports NBA stats

# Note - block must be copied into ipython --pylab
# Note - Currently unsure as to the cause of the dips in 1999 and 2012

from pandas import DataFrame, Series
import pandas as pd

columns = ['id', 'Year','Player','Pos','Age','Tm','G','GS','MP','PER','TS%','3PAr','FTr','ORB%','DRB%','TRB%','AST%','STL%','BLK%','TOV%','USG%','blanl','OWS','DWS','WS','WS/48','blank2','OBPM','DBPM','BPM','VORP','FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','eFG%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS']
path = '/Users/Jason/NBA_Statistical_Analysis/datasets/Seasons_Stats.csv'
frame = pd.read_csv(path, names=columns)
frame = frame.drop(0)
delCols=['id', 'blanl', 'blank2']
for col in delCols:
    del frame[col]
convCols = ['Year', 'Age', 'G', 'GS', 'MP', 'PER', 'TS%', '3PAr','FTr','ORB%','DRB%','TRB%','AST%','STL%','BLK%','TOV%','USG%','OWS','DWS','WS','WS/48','OBPM','DBPM','BPM','VORP','FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','eFG%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS']
for col in convCols:
    frame[col] = pd.to_numeric(frame[col])
frame = frame[frame['Tm'] != 'TOT'] # Remove Total rows for players that were with more than one team for a season

teamsList = [17]+[11]+[10]*2+[9]*2+[8]*6+[9]*5+[10]+[12]+[14]*2+[17]*4+[18]*2+[22]*4+[23]*8+[25]+[27]*6+[29]*9+[30]*13
gamesPlayedList = [60]*18+[82]*50

years = range(1980, 2018)
attemptList = []
for year in years:
    attempts = frame.loc[frame['Year'] == year, '3PA'].sum()
    teams = teamsList[year-1950]
    attemptsPerTeam = attempts/teams
    attemptsPerTeamPerGame = attemptsPerTeam / gamesPlayedList[year-1950]
    attemptList.append(attemptsPerTeamPerGame)

matplotlib.pyplot.bar(years, attemptList)
matplotlib.pyplot.xlabel("Year")
matplotlib.pyplot.ylabel("3P Attempts Per Game")
matplotlib.pyplot.title("3P Attempts Per Game by Year")