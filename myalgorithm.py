import re

# Class WeightedGraph
class WeightedGraph:
    def __init__(self, path):
        # open file to initialize the graph
        file = open('graph_41.txt', "r")
        p = re.compile("\d+")

        # initialize the graph
        self.vertices, self.edges = map(int, p.findall(file.readline()))
        # use adjacent matrix to represent the graph
        self.graph = [[0]*self.vertices for _ in range(self.vertices)]

        # populate the graph
        for i in range(self.edges):
            u, v, weight = map(int, p.findall(file.readline()))
            self.graph[u][v] = weight
            self.graph[v][u] = weight


# Union find data structure for quick kruskal algorithm
class UF:
    def __init__(self, N):
        self._id = [i for i in range(N)]

    # judge two node connected or not
    def connected(self, p, q):
        return self._find(p) == self._find(q)

  # quick union two component
    def union(self, p, q):
        p_root = self._find(p)
        q_root = self._find(q)
        if p_root == q_root:
            return
        self._id[p_root] = q_root

    # find the root of p
    def _find(self, p):
        while p != self._id[p]:
            p = self._id[p]
        return p

# kruskal algorithm
def kruskal(G):
    # initialize MST
    MST = set()
    edges = set()
    # collect all edges from graph G
    for j in range(G.vertices):
        for k in range(G.vertices):
            if G.graph[j][k] != 0 and (k, j) not in edges:
                edges.add((j, k))
    # sort all edges in graph G by weights from smallest to largest
    sorted_edges = sorted(edges, key=lambda e:G.graph[e[0]][e[1]])
    uf = UF(G.vertices)for e in sorted_edges:
    u, v = e
        # if u, v already connected, abort this edge
        if uf.connected(u, v):
            continue
        # if not, connect them and add this edge to the MST
        uf.union(u, v)
        MST.add(e)
    return MST
    for MST in p:
	print(MST)
