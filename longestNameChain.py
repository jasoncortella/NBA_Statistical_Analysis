#!/Users/Jason/anaconda3/bin/python3

import numpy as np
import pandas as pd
import os

path = '/Users/Jason/NBA_Statistical_Analysis/datasets/Players.csv'
data = pd.read_csv(path)
names = data['Player'].str.split(' ',expand=True)
names.columns = ['first', 'last']
names = names.dropna() # Removes Nene
names = names[names['first'] != names['last']] # Removes Ha Ha and Sun Sun

import networkx as nx
G = nx.DiGraph()
G.add_nodes_from(list(names['first']))
G.add_nodes_from(list(names['last']))
# Add edges
G.add_edges_from(list(zip(names['first'],names['last'])))
x = ' '.join(nx.dag_longest_path(G))
print(x)