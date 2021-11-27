import UtilityFunctions as utilf
import algorithmic_complexity.util as util
import algorithmic_complexity.disjointset as ds
import heapq as hq

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
    
    i = 0
    for node in newG:
        j = 0
        for conec in node:
            if conec[0] < indexes[0]:
                print(newG[i].pop(j))
            j += 1
        i += 1
    
    artMaxH = len(range(minX, maxX+1))
    artMaxV = len(range(minY, maxY+1))
    
    return [newG, indexes, nc, artMaxH, artMaxV]

def kruskal(G):
  n = len(G)
  edges = []
  for u in range(n):
    for v, w in G[u]:
      hq.heappush(edges, (w, u, v))

  uf = ds.DisjointSet(n)

  T = []
  while edges and n > 0:
    w, u, v = hq.heappop(edges)
    if not uf.sameset(u, v):
      uf.union(u, v)
      T.append((u, v, w))
      n -= 1

  return T

Nodes = utilf.retrieveInfoFromDataset_v1()
g = utilf.reconstructDataset_v2(Nodes, 1000, 1000)
types = Nodes[1]
del Nodes

'''
Se usará el algoritmo de Kruskal para generar un árbol de expansión mínimo, pero habrá un ligero
cambio para poder iniciar con un determinado nodo (que sería el del punto de almacén) y así generar
la ruta más corta desde el punto de almacén hacia todos los puntos de entrega
'''

def algoritmoDeHugo():
  Types, G, maxH, maxV = generateRectangularGraph(d=1, v=5, h=20, eDensity=0.5)
  print("█", end=" ")
  print(Types, G, maxH, maxV, sep="\n\n ")
  #print(G)

  # Buscamos el nodo almacén en el grafo

  x = 0

  for element in Types:
    if element.split('.')[3] == 'd':
      nodoAlmacen = Types[x]
    x = x + 1

  print(nodoAlmacen)

  #arbol = kruskal(G, nodoAlmacen)

algoritmoDeHugo()
