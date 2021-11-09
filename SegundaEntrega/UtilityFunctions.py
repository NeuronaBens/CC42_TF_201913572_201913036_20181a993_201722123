import random
import csv
import numpy as np

def findNPerCoordinates(x, y, Vmax, Hmax):
    if y >= Vmax or y < 0:
        return None
    if x >= Hmax or x < 0:
        return None
    N = x*Vmax + y
    return N

def findCoordinatesPerN(N, maxV):
    y = N%maxV
    x = (N-y)/maxV
    return x, y


def generateRectangularGraph(d=None, v=None, h=None, eDensity=0.5):
    dist_points = random.randrange(50, 100)
    if d is not None:
        dist_points = d
    vertical = random.randrange(10, 140)
    if v is not None:
        vertical = v
    horizontal = int(3500/vertical)
    if h is not None:
        horizontal = h
    
    qnodes = vertical * horizontal
    
    nOfE = int((qnodes-dist_points)*0.5)
    nOfN = qnodes - dist_points - nOfE
    
    point_list = ["d"]*dist_points + ["e"]*(nOfE) + ["n"]*(nOfN)
    random.shuffle(point_list)
    n = 0
    
    for x in range(horizontal):
        for y in range(vertical):
            point_list[n] = str(n) + "." + str(x) + "." + str(y) + "." + point_list[n]
            n+=1
    
    adj_list = list()
    for elem in point_list:
        aux = elem.split(".")
        x = int(aux[1])
        y = int(aux[2])
        p_up = findNPerCoordinates(x, y-1, vertical, horizontal)
        p_down = findNPerCoordinates(x, y+1, vertical, horizontal)
        p_left = findNPerCoordinates(x-1, y, vertical, horizontal)
        p_right = findNPerCoordinates(x+1, y, vertical, horizontal)
        innerlist = list()
        if p_up is not None:
            innerlist.append((p_up, random.randrange(1, 10)))
        if p_down is not None:
            innerlist.append((p_down, random.randrange(1, 10)))
        if p_left is not None:
            innerlist.append((p_left, random.randrange(1, 10)))
        if p_right is not None:
            innerlist.append((p_right, random.randrange(1, 10)))
        adj_list.append(innerlist)

    return point_list, adj_list, horizontal, vertical

def getCost(d, t):
    return d + 0.1*(t*t)

def availableNodesByDir(n, G, h, v):
    adj_nodes = G[n]
    dirs = list()
    for node in adj_nodes:
        if node[0] == n-1:
            dirs.append("up")
        elif node[0] == n+v:
            dirs.append("right")
        elif node[0] == n-v:
            dirs.append("left")
        elif node[0] == n+1:
            dirs.append("down")
    return dirs

def getNodeByDir(n, maxV, Dir): #la condicionalidad de si existe el nodo o no, no ocurre dentro de esta función
    if Dir == "up": #esta función permite definir por ejemplo que nodo está Arriba 
        return n - 1 #de 11 en un grafo rectangular de 3x4, sería 10
    if Dir == "down":
        return n + 1
    if Dir == "left":
        return n - maxV # en 3x4, si nos piden izquierda de 11 sería 7
    if Dir == "right":
        return n + maxV
    

def stringInList(string, lst):
    i = 0
    for e in lst:
        if string == e:
            return True, i
        i+=1
    return False, -1

def calculateWorstPath(G, h, v):
    d = (v-1)*h
    t = 0
    next_dir = "down"
    n = 0
    for nodes in G:
        adj_dirs = availableNodesByDir(n, G, h, v)
        isin, pos = stringInList(next_dir, adj_dirs)
        if isin:
            t += nodes[pos][1]
        n+=1
    return getCost(d, t) + (h-1)*5 + h #para simular pasar de un nodo a otro horizontalmente

def listToString(ll, forbidden="\n"):
    string = ""
    for x in ll:
        if x == forbidden:
            continue
        string += x
    return string

def stringReplacer(string, charTR, replacement):
    newString=""
    for x in string:
        if x == charTR:
            newString += replacement
        else:
            newString += x
    return newString

def pointTo4ElementList(pointString, delimiter="."):
    return pointString.split(delimiter)

def retrieveInfoFromDataset_v1(): #esta versión permite extraer los nodos del archivo "totalidad_de_puntos.csv"
    N = np.zeros((1000000, 3), dtype=int)
    Types = [None]*1000000
    with open("totalidad_de_puntos.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        i = 0
        j = 0
        next(reader)
        next(reader)
        for line in reader:
            i+=1
            if i%2==0:
                continue
            N[j][0] = int(line[0])
            N[j][1] = int(line[1])
            N[j][2] = int(line[2])
            Types[j] = line[3]
            j+=1
    return N, Types #N tiene los pares x, y y Types tiene de que tipo es cada nodo

def reconstructDataset_v1(N, maxV, maxH): #si es de 1000x1000 maxV y maxH son 1000, 1000
    G = [None]*(maxV*maxH)
    i = 0
    for node in N[0]:
        posibleDirs = [True, True, True, True] # "up", "down", "left", "right"
        if node[1] <= 0:
            posibleDirs[2] = False
        if node[2] <= 0:
            posibleDirs[0] = False 
        if node[1] >= maxH - 1:
            posibleDirs[3] = False
        if node[2] >= maxV - 1:
            posibleDirs[1] = False
        aux = []
        if posibleDirs[0]:
            aux.append(getNodeByDir(node[0], maxV, "up"))
        if posibleDirs[1]:
            aux.append(getNodeByDir(node[0], maxV, "down"))
        if posibleDirs[2]:
            aux.append(getNodeByDir(node[0], maxV, "left"))
        if posibleDirs[3]:
            aux.append(getNodeByDir(node[0], maxV, "right"))
        
        G[i] = aux
        i+=1
    return G

def reconstructDataset_v2(N, maxV, maxH): #si es de 1000x1000 maxV y maxH son 1000, 1000
    G = [None]*(maxV*maxH)
    i = 0
    for node in N[0]:
        posibleDirs = [True, True, True, True] # "up", "down", "left", "right"
        if node[1] <= 0:
            posibleDirs[2] = False
        if node[2] <= 0:
            posibleDirs[0] = False 
        if node[1] >= maxH - 1:
            posibleDirs[3] = False
        if node[2] >= maxV - 1:
            posibleDirs[1] = False
        aux = []
        if posibleDirs[0]:
            aux.append((getNodeByDir(node[0], maxV, "up"), random.randint(1, 10)))
        if posibleDirs[1]:
            aux.append((getNodeByDir(node[0], maxV, "down"), random.randint(1, 10)))
        if posibleDirs[2]:
            aux.append((getNodeByDir(node[0], maxV, "left"), random.randint(1, 10)))
        if posibleDirs[3]:
            aux.append((getNodeByDir(node[0], maxV, "right"), random.randint(1, 10)))
        
        G[i] = aux
        i+=1
    return G

############################################################

#pl, G, h, v = generateRectangularGraph(2, 12, 12)
'''
Nodes = retrieveInfoFromDataset_v1()
'''

'''
Nodes = [[0, 0, 0], [1, 0, 1], [2, 0, 2],
         [3, 1, 0], [4, 1, 1], [5, 1, 2],
         [6, 2, 0], [7, 2, 1], [8, 2, 2]]
'''

'''
g = reconstructDataset_v1(Nodes, 1000, 1000)
'''

'''
with open("totalidad_de_puntos.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    ll = ["name", "x", "y", "type"]
    writer.writerow(ll)
    for point in pl:
        writer.writerow(pointTo4ElementList(point))

with open("almacenes.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    ll = ["x", "y"]
    writer.writerow(ll)
    index=0
    while index < len(pl):
        x = pointTo4ElementList(pl[index])
        if x[3] == "d":
            writer.writerow(x[1:3])
        index+=1

with open("puntos_entrega.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    ll = ["x", "y"]
    writer.writerow(ll)
    index=0
    while index < len(pl):
        x = pointTo4ElementList(pl[index])
        if x[3] == "e":
            writer.writerow(x[1:3])
        index+=1
'''
