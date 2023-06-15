from collections import defaultdict


def build_graph(edge_list):
    graph = defaultdict(list)
    seen_edges = defaultdict(int)
    for src, dst, weight in edge_list:
        seen_edges[(src, dst, weight)] += 1
        if seen_edges[(src, dst, weight)] > 1:  # checking for duplicated edge entries
            continue
        graph[src].append((dst, weight))
        graph[dst].append((src, weight))  # remove this line of edge list is directed
    return graph


def dijkstra(graph, src, dst=None):
    nodes = []
    for n in graph:
        nodes.append(n)
        nodes += [x[0] for x in graph[n]]

    q = set(nodes)
    nodes = list(q)
    dist = dict()
    prev = dict()
    for n in nodes:
        dist[n] = float('inf')
        prev[n] = None

    dist[src] = 0

    while q:
        u = min(q, key=dist.get)
        q.remove(u)

        if dst is not None and u == dst:
            return dist[dst], prev

        for v, w in graph.get(u, ()):
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev


def find_path(pr, node):  # generate path list based on parent points 'prev'
    p = []
    while node is not None:
        p.append(node)
        node = pr[node]
    return p[::-1]


if __name__ == "__main__":
    edges = [
        ["A", "S", 4],
        ["A", "D", 5],
        ["A", "E", 3],
        ("S", "B", 5),
        ("S", "D", 11),
        ("S", "C", 10),
        ("D", "E", 2),
        ("D", "F", 5),
        ("D", "C", 3),
        ("C", "B", 8),
        ("C", "F", 2),
        ("B", "F", 9),
        ("F", "E", 4),
        ("F", "G", 7),
        ("E", "G", 8)

    ]

    g = build_graph(edges)

    print("=== Dijkstra ===")

    print("--- Single source, single destination ---")
    # d, prev = dijkstra(g, "F", "G")
    # path = find_path(prev, "E")
    # print("A -> E: distance = {}, path = {}".format(d, path))

    d, prev = dijkstra(g, "S", "G")
    path = find_path(prev, "G")
    print("S -> G: distance = {}, path = {}".format(d, path))

    print("--- Single source, all destinations ---")
    ds, prev = dijkstra(g, "S")
    for k in ds:
        path = find_path(prev, k)
        print("S -> {}: distance = {}, path = {}".format(k, ds[k], path))