import random
import csv
import numpy as np
import math

def findNPerCoordinates(x, y, Vmax, Hmax):
    if y >= Vmax or y < 0:
        return None
    if x >= Hmax or x < 0:
        return None
    N = x*Vmax + y
    return N

def nodeOutOfCuadrangularLimit_byN(N, centerN, toSideSize, maxH, maxV):
    x, y = findCoordinatesPerN(centerN, maxV)
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
    
    nxy = findCoordinatesPerN(N, maxV)
    if(nxy[0] > maxX):
        return True
    if(nxy[0] < minX):
        return True
    if(nxy[1] > maxY):
        return True
    if(nxy[1] < minY):
        return True
    
    return False


def findCoordinatesPerN(N, maxV):
    y = N%maxV
    x = (N-y)/maxV
    return int(x), int(y)

def euclidianDistanceFromNodeToNode(i, j, maxV): #j e i son los nombres, indices de los nodos en cuestion
    pair1 = findCoordinatesPerN(i, maxV)
    pair2 = findCoordinatesPerN(j, maxV)
    dx = pair1[0] - pair2[0]
    dy = pair1[1] - pair2[1]
    d = math.sqrt(dx**2 + dy**2)
    return d

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

################################################################

def nodeToLeft(current, maxV, maxH):
    if current + maxV >= maxV*maxH:
        return None
    else:
        return current + maxV

def nodeToRight(current, maxV, maxH):
    if current - maxV < 0:
        return None
    else:
        return current - maxV

def nodeToUp(current, maxV, maxH):
    if (current - 1) < int(current/maxV)*maxV:
        return None
    else:
        return current - 1

def nodeToDown(current, maxV, maxH):
    if (current + 1) % maxV == 0:
        return None
    if current + 1 >= maxV*maxH:
        return None
    return current + 1

def furthestUnvisitedRightNode(current, maxV, maxH, visited):
    aux = current
    reps = 0
    while True:
        nextNode = nodeToRight(aux, maxV, maxH)
        if nextNode is not None and visited[nextNode] == False:
            aux = nextNode
        else:
            return aux
        if reps >= 1e6:
            raise Exception('reps went to 1 million, makes no sense')
        reps += 1
    raise Exception('makes no sense there is no return in fURN function')

def furthestUnvisitedLeftNode(current, maxV, maxH, visited):
    aux = current
    while True:
        nextNode = nodeToLeft(aux, maxV, maxH)
        if nextNode is None:
            return aux
        if visited[nextNode] == True:
            return aux
        aux = nextNode

def AlgoritmoDeGabriel(G, Type, maxV, maxH):
    dists = []
    visited = [False]*maxV*maxH
    parents = [None]*maxV*maxH
    
    j = 0
    for i in Type:
        aux = i.split(".")
        if aux[3] == "d":
            dists.append(j)
            visited[j] = False
            parents[j] = j
        j += 1
    
    for i in dists:
        aux = i
        while True:
            nextNode = nodeToUp(aux, maxV, maxH) 
            if nextNode is not None and visited[nextNode] == False:
                visited[nextNode] = True
                parents[nextNode] = aux
                aux = nextNode
            else:
                aux = i
                break
        while True:
            nextNode = nodeToDown(aux, maxV, maxH) 
            if nextNode is not None and visited[nextNode] == False:
                visited[nextNode] = True
                parents[nextNode] = aux
                aux = nextNode
            else:
                aux = i
                break
    
    for i in dists:
        kk = True
        while kk == True:
            j = furthestUnvisitedLeftNode(i, maxV, maxH, visited)
            
            if j == i:
                kk = False
            else:
                aux = j
                visited[aux] = True
                parents[aux] = nodeToRight(aux, maxV, maxH)
                ff = True
                
                while ff == True: #complete copy from line 89
                    nextNode = nodeToUp(aux, maxV, maxH) 
                    if nextNode is not None:
                        visited[nextNode] = True
                        parents[nextNode] = aux
                        aux = nextNode
                    else:
                        aux = i
                        ff = False
                ff = True
                aux = j
                while ff == True: #complete copy from line 89
                    nextNode = nodeToDown(aux, maxV, maxH) 
                    if nextNode is not None:
                        visited[nextNode] = True
                        parents[nextNode] = aux
                        aux = nextNode
                    else:
                        aux = i
                        ff = False
                    kk = True
        kk = True
        while kk == True:
            j = furthestUnvisitedRightNode(i, maxV, maxH, visited)
            
            if j == i:
                kk = False
            else:
                aux = j
                visited[aux] = True
                parents[aux] = nodeToLeft(aux, maxV, maxH)
                ff = True
                
                while ff == True: #complete copy from line 89
                    nextNode = nodeToUp(aux, maxV, maxH) 
                    if nextNode is not None:
                        visited[nextNode] = True
                        parents[nextNode] = aux
                        aux = nextNode
                    else:
                        aux = i
                        ff = False
                ff = True
                aux = j
                while ff == True: #complete copy from line 89
                    nextNode = nodeToDown(aux, maxV, maxH) 
                    if nextNode is not None:
                        visited[nextNode] = True
                        parents[nextNode] = aux
                        aux = nextNode
                    else:
                        aux = i
                        ff = False
    return parents


Types, G, maxH, maxV = generateRectangularGraph(d=3, v=8, h=11, eDensity=0.5)

print("█", end=" ")
print(Types, G, maxH, maxV, sep="\n\n█ ")
print(end="\n\n\n")

x = AlgoritmoDeGabriel(G, Types, maxV, maxH)

for i in range(maxH):
    for j in range(maxV):
        print(x[i*maxV+j], end="\t ")
    print()

for i in range(maxH):
    for j in range(maxV):
        print(Types[i*maxV+j], end=" ")
    print()


