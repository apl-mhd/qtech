import heapq as hq
from operator import le
from turtle import distance

graph = {
    'Rabat': ('Sueca', 1063),
    'Sueca': ('Rudow', 2656),
    'Rudow': ('Mosu', 1352),
    'Mosu' : ('Le Plessis Trevise', 100),
    'Le Plessis Trevise': ('Kang Dong', 61),
    'Kang Dong': ('Nezahualcóyotl', 1634),
    'Nezahualcóyotl': ('Lindenwold', 151),
    'Lindenwold': ('Queanbeyan', 285),
    'Queanbeyan': ('Saint Chamond', 146),
    'Saint Chamond': ('Cheektowaga', 11),
    'Cheektowaga': ('Tirupati', 347),
    'Tirupati': ('Snezhinsk', 2547),
    'Snezhinsk': ('Glazov', 2524),
    'Glazov': ('Gaoyou', 97),
    'Gaoyou': ('Nola', 6999),
    'Nola': ('Rutigliano', 63),
    'Rutigliano': ('Colombo', 105),
    'Colombo': ('Meckenheim', 244),
    'Meckenheim': ('Hamburg', 502),
    'Hamburg': ('Rabat', 30),


}

visited = {}
distance = {}



def graph_init(source):

    for i in graph:
        visited[i] = False
        #distance[i] = 999999
    
    #visited[source] = True
    distance[source] = 0



def distance_calculate(source):
    graph_init(source)
    pq = []
    
    pq.append(tuple(( 0, source)))

    while(len(pq)):
        p = pq.pop(0)
        u = p[1] # u
        uwt = p[0] # u Weight
        visited[u] = True
        d = graph[u] # u to v vartex
        v = d[0]

        if visited[v] == False:
            uvwt = d[1] # u to v weight
            total_wt = uwt + uvwt
            distance[v] = total_wt
            pq.append(tuple((total_wt, v)))


distance_calculate('Rabat')

for i in distance:
    print(i,' : ',distance[i])

