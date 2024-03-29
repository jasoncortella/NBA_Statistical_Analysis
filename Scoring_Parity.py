# Compares the avg ppg totals of top [specified] scorers by season

# Note - block must be copied into ipython --pylab

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

frame.insert(2, 'PPG', frame['PTS']/frame['G']) 

years = range(1950, 2018)
scorers = 5 # Select the number of scorers
scorerList = []

for year in years:
    topScorers = frame.loc[frame['Year'] == year, 'PPG'].nlargest(scorers)
    topScorersAvg = topScorers.sum()/scorers
    scorerList.append(topScorersAvg)

p1 = matplotlib.pyplot.bar(years, scorerList)
matplotlib.pyplot.xlabel("Year")
matplotlib.pyplot.ylabel("AVG PPG of top {} scorers".format(scorers))
matplotlib.pyplot.title("NBA Scoring Parity")