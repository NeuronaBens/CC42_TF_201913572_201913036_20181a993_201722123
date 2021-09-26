import random

def findNPerCoordinates(x, y, Vmax, Hmax):
    if x >= Vmax or x < 0:
        return None
    if y >= Hmax or y < 0:
        return None
    N = x*Vmax + y
    return N

def generateRectangularGraph(d=None, v=None, h=None):
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
    point_list = ["d"]*dist_points + ["e"]*(qnodes-dist_points)
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


pl, al, h, v = generateRectangularGraph(1, 4, 4)
print(pl)
print(al)
print(h)
print(v)
    
