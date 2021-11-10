import UtilityFunctions as uf

Nodes = uf.retrieveInfoFromDataset_v1()
g = uf.reconstructDataset_v2(Nodes, 1000, 1000)
types = Nodes[1]
del Nodes
print(types[0:5])
print(g[0:5])


import numpy as np
import pandas as pd
import heapq as hq
import math

def dijkstra(G, s):
  n = len(G)
  visited = [False]*n
  path = [None]*n
  cost = [math.inf]*n
  cost[s] = 0
  queue = [(0, s)]
  while queue:
    g_u, u = hq.heappop(queue)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        f = g_u + w
        if f < cost[v]:
          cost[v] = f
          path[v] = u
          hq.heappush(queue, (f, v))

  return path, cost

def createRectangularSubGraph(G, center, toSideSize, maxH, maxV):
    x, y = uf.findCoordinatesPerN(center, maxV)
    minX = x - toSideSize
    maxX = x + toSideSize
    minY = y - toSideSize
    maxY = y + toSideSize
    
    if minX < 0:
        minX = 0
    if maxX >= maxH:
        maxX = maxH - 1
    if minY < 0:
        minY = 0
    if maxY >= maxV:
        maxY = maxV - 1
    
    maxX = int(maxX)
    minX = int(minX)
    maxY = int(maxY)
    minY = int(minY)
    
    nc = None
    c = 0
    
    indexes = []
    for i in range(minX, maxX+1):
        for j in range(minY, maxY+1):
            indexes.append(uf.findNPerCoordinates(i, j, maxV, maxH))
            if indexes[-1] == center:
                nc = c
            c += 1
    
    newG = []
    for i in indexes:
        newG.append(G[i])
        j = 0
        for conec in newG[-1]:
            if uf.nodeOutOfCuadrangularLimit_byN(conec[0], center, toSideSize, maxH, maxV):
                newG[-1].pop(j)
            j+=1
    
    return newG, indexes, nc
    

print(createRectangularSubGraph(g, 1001, 5, 1000, 1000))


###########
#BFS partiendo desde los puntos de almacén
#types contiene los tipos de puntos siendo 499750 vacíos (n), 499750 puntos de entrega (e) y 500 puntos de almacén (d)
#Se recorrerá types para identificar los index de los nodos en los que sean de almacén y luego con esto realizar el BFS partiendo desde este punto

index = 0
for i in types:
  if i == 'd':
    newg = createRectangularSubGraph(g, index, 5, 1000, 1000) #5 de distancia a los lados de cada punto de distribución 
    path = dijkstra(newg[0], newg[2])
    print(path)
  index = index + 1

#no funciona porque g[x][y] == 1000 por ejemplo, aun siendo el grafo de 10 x 10
