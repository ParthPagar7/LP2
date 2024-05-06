class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_algo(self):
        key = [float('inf')] * self.V
        parent = [-1] * self.V
        mst_set = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v, weight in self.graph[u]:
                if not mst_set[v] and weight < key[v]:
                    parent[v] = u
                    key[v] = weight

        minimum_cost = sum(key[1:])  # Total cost of MST excluding the root node
        
        self.print_mst(parent)
        
        return minimum_cost

    def min_key(self, key, mst_set):
        min_val = float('inf')
        min_index = -1

        for v in range(self.V):
            if not mst_set[v] and key[v] < min_val:
                min_val = key[v]
                min_index = v

        return min_index

    def print_mst(self, parent):
        print('\nPrim’s Minimum Spanning Tree:')
        print('Edge \tWeight')
        for i in range(1, self.V):
            print(f"{parent[i]} - {i}\t{self.get_weight(parent[i], i)}")

    def get_weight(self, u, v):
        for vertex, weight in self.graph[u]:
            if vertex == v:
                return weight
        return 0

g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 4, 3)
g.add_edge(5, 4, 3)
min_cost = g.prim_algo()
print("Minimum cost of the MST:", min_cost)
