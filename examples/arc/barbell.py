"""
Displays a NetworkX barbell graph to screen using a ArcPlot.
"""

from nxviz.plots import ArcPlot
from random import choice
import networkx as nx
import matplotlib.pyplot as plt

G = nx.barbell_graph(m1=10, m2=3)
for n, d in G.nodes(data=True):
    G.node[n]['class'] = choice(['one', 'two', 'three'])
c = ArcPlot(G, node_color="class", node_order='class')
c.draw()
plt.show()
