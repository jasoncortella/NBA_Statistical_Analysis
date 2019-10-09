# Basic BabyName analysis - Plots the number of births per year of a specified name

# Note - block must be copied into ipython --pylab

from pandas import DataFrame, Series
import pandas as pd

columns = ['id', 'Player', 'height', 'weight', 'collage', 'born', 'birth_city', 'birth_state']
path = '/Users/Jason/NBA_Statistical_Analysis/datasets/Players.csv'
frame = pd.read_csv(path, names=columns)
del frame['id']
frame = frame.drop(0)
convCols = ['height', 'weight', 'born']
for col in convCols:
    frame[col] = pd.to_numeric(frame[col])
frame.plot.scatter(x='born', y='height', title='Player Height as a Function of Birth Year')