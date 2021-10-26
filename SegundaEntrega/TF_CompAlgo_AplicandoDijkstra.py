import UtilityFunctions as uf

Nodes = uf.retrieveInfoFromDataset_v1()

g = uf.reconstructDataset_v1(Nodes, 1000, 1000)

types = Nodes[1]

del Nodes

print(types[0:5])

print(g[0:5])

