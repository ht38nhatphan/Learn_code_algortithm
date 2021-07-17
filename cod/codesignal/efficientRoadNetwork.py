from collections import defaultdict


# def build_graph(edge_list):
#     graph = defaultdict(list)
#     seen_edges = defaultdict(int)
#     for src, dst, weight in edge_list:
#         seen_edges[(src, dst, weight)] += 1
#         if seen_edges[(src, dst, weight)] > 1:  # checking for duplicated edge entries
#             continue
#         graph[src].append((dst, weight))
#         graph[dst].append((src, weight))  # remove this line of edge list is directed
#     return graph


# def dijkstra(graph, src, dst=None):
#     nodes = []
#     for n in graph:
#         nodes.append(n)
#         nodes += [x[0] for x in graph[n]]

#     q = set(nodes)
#     nodes = list(q)
#     dist = dict()
#     prev = dict()
#     for n in nodes:
#         dist[n] = float('inf')
#         prev[n] = None

#     dist[src] = 0

#     while q:
#         u = min(q, key=dist.get)
#         q.remove(u)

#         if dst is not None and u == dst:
#             return dist[dst], prev

#         for v, w in graph.get(u, ()):
#             alt = dist[u] + w
#             if alt < dist[v]:
#                 dist[v] = alt
#                 prev[v] = u

#     return dist, prev


# def find_path(pr, node):  # generate path list based on parent points 'prev'
#     p = []
#     while node is not None:
#         p.append(node)
#         node = pr[node]
#     return p[::-1]
# def efficientRoadNetwork(n, roads):
#     if n == 1:
#         return True
#     for i in range(len(roads)):
#         roads[i].append(1)
#     g = build_graph(roads)
#     for i in range(n):
#         ds, prev = dijkstra(g, i)
#         for i in ds:
#             # print(ds)
#             if(ds[i]>2):
#                 return False
#         # print(ds)
#     return len(ds)==n and True or False
def efficientRoadNetwork(n, roads):
    adj = [[] for i in range(n)]
    for rd in roads:
        adj[rd[0]].append(rd[1])
        adj[rd[1]].append(rd[0])
    for city in range(n - 1):
        oneHop = {c for c in adj[city]}
        twoHops = {c for c1 in oneHop for c in adj[c1]}    
        if len({city} | oneHop | twoHops) < n:
            return False
    return True

print(efficientRoadNetwork(2,[[0,1]]))

