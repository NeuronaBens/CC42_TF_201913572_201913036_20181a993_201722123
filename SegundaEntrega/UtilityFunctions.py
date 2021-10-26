import random
import csv

def findNPerCoordinates(x, y, Vmax, Hmax):
    if y >= Vmax or y < 0:
        return None
    if x >= Hmax or x < 0:
        return None
    N = x*Vmax + y
    return N
    

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
            
############################################################

pl, G, h, v = generateRectangularGraph(500, 1000, 1000)


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
