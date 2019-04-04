class Vertex:
    def __init__(self, key):
        self.key = key
        self.adjacent = {}

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def addNeighbour(self, neighbour, weight=0):
        self.adjacent[neighbour] = weight

    def getNeighbours(self):
        return self.adjacent.keys()

    def getWeight(self, neighbour):
        return self.adjacent[neighbour]


class Graph:
    def __init__(self):
        self.vertices = {}
        self.numberOfVertices = 0
    
    def num_vertices(self):
	return self.numberOfVertices

    def num_edges(self):
        edges = self.edges()
        cnt = 0
        for edgeSet in edges:
            cnt += len(edgeSet)
        
        return cnt
    
    def add_vertex(self, v):
        node = Vertex(v)
        self.vertices[v] = node
        self.numberOfVertices += 1
        return node

    def add_edge(self, u, v, w=0):
        if u not in self.vertices:
            self.add_vertex(u)

        if v not in self.vertices:
            self.add_vertex(v)

        self.vertices[u].addNeighbour(self.vertices[v], w)

    def get_vertex(self, v):
        if v in self.vertices:
            return self.vertices[v]
        else:
            return None
    
    def get_edge(self, u, v):
        if u in self.vertices or v in self.vertices:
	   return None

	for w in self.vertices[v].getNeighbours():
            frm = self.vertices[v].getKey()
            to = w.getKey()
            weight = self.vertices[v].getWeight(w)
            if to == u:
                return (frm, to, weight)
        
        return None
    
    def vertices(self):
        return self.vertices.keys()

    def edges(self):
        edges = []
        for v in self.vertices:
            edgesFromVertex = []

            for w in self.vertices[v].getNeighbours():
                frm = self.vertices[v].getKey()
                to = w.getKey()
                weight = self.vertices[v].getWeight(w)
		edgesFromVertex.append((frm, to, weight))


            if len(edgesFromVertex) != 0:
                edges.append(edgesFromVertex)

        return edges
    
    def adj_vertices(self, v):
        l = []
        vertex = self.get_vertex(v)
        if vertex != None:
            for n in vertex.getNeighbours():
                l.append(n.getKey())
            return l
        
        return None

#Example used class Graph
if __name__ == '__main__':
	g = Graph()
	g.add_vertex('a')
    	g.add_vertex('b')
    	g.add_vertex('c')
    	g.add_vertex('d')
    	g.add_vertex('e')
    	g.add_vertex('f')
    	g.add_edge('a', 'b', 3)
    	g.add_edge('b', 'c', 2)
    	g.add_edge('c', 'd', 1)
    	g.add_edge('d', 'e', 5)
    	g.add_edge('d', 'a', 5)
    	g.add_edge('d', 'a', 2)
    	g.add_edge('e', 'f', 3)
    	g.add_edge('f', 'a', 6)
    	g.add_edge('f', 'b', 6)
    	g.add_edge('f', 'c', 6)
    
    print("Num Vertices", g.num_vertices())
    print("Num Edges", g.num_edges())
    print("Vertex 'a' =", g.get_vertex('a').getKey())
    print("Edge two vertices 'a' and 'd' =", g.get_edge('a', 'd'))
    print("Adjacent for f =", g.adj_vertices('f'))
    print()
    #print all edges
    for edgeSet in g.edges():
        print('edges from', edgeSet[0][0] + ': ', end='')
	print(edgeSet)
