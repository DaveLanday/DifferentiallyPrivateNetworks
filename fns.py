from dpnet import load_mtx
import networkx as nx

karate = nx.karate_club_graph()
n = karate.nodes
e = karate.edges
tmp = 0
d = {}
count = 0
print(n)

for i in range(len(n)):
    d[i] = 0

for i in e:
    if i[0] != tmp:
        d[tmp] = count
        tmp = i[0]
        count = 1
    else:
        count += 1

print(d)

print(len(n))


#for i in range(len(karate.edges)):
 #   for j in range(len(i)):
