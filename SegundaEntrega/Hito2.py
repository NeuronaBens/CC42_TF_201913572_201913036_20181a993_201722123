import graphviz as gv
import numpy as np
import pandas as pd
import heapq as hq
import math

def bfs(G, s):
  n = len(G)
  visited = [False]*n
  parent = [None]*n
  queue = [s]
  visited[s] = True

  while queue:
    u = queue.pop(0)
    for v in G[u]:
      if not visited[v]:
        visited[v] = True
        parent[v] = u
        queue.append(v)

  return parent

import UtilityFunctions as uf

Nodes = uf.retrieveInfoFromDataset_v1()

G = uf.reconstructDataset_v1(Nodes, 1000, 1000)

types = Nodes[1]

del Nodes

print(G[0:10])

#Hito 2

path = bfs(G, 0) #partiendo desde el nodo 0

print(path)

#BFS partiendo desde los puntos de almacén
#types contiene los tipos de puntos siendo 499750 vacíos (n), 499750 puntos de entrega (e) y 500 puntos de almacén (d)
#Se recorrerá types para identificar los index de los nodos en los que sean de almacén y luego con esto realizar el BFS partiendo desde este punto

index = 0
for i in types:
  if i == 'd':
    path = bfs(G, index)
    print(path)
  index = index + 1
