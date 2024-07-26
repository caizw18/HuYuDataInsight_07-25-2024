class UnionFind:
    def __init__(self, size):
        # Initialize the parent array where each node is its own parent
        self.parent = list(range(size))
        # Initialize the rank array to keep track of the tree depth
        self.rank = [1] * size

    def find(self, u):
        # Path compression optimization
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # Find roots of the sets to which u and v belong
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank optimization
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

    def connected(self, u, v):
        return self.find(u) == self.find(v)

# Example usage of Union-Find
def main():
    n = 10  # Number of elements
    uf = UnionFind(n)

    # Perform some union operations
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(4, 5)
    uf.union(5, 6)
    uf.union(1, 5)

    # Check connections
    print(uf.connected(1, 6))  # Output: True
    print(uf.connected(1, 7))  # Output: False

if __name__ == "__main__":
    main()


def large_sparse_graph_example():
    n = 1000000  # 1,000,000 nodes
    uf = UnionFind(n)

    # Add 10 edges
    edges = [
        (1, 2), (2, 3), (4, 5), (6, 7), (8, 9),
        (10, 11), (12, 13), (14, 15), (16, 17), (18, 19)
    ]

    for u, v in edges:
        uf.union(u, v)

    # Check connectivity
    print(uf.connected(1, 3))  # Output: True
    print(uf.connected(1, 5))  # Output: False


large_sparse_graph_example()


def dynamic_connectivity_example():
    n = 10  # Number of nodes
    uf = UnionFind(n)

    # Initially, no edges
    print(uf.connected(0, 1))  # Output: False

    # Add edges
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(4, 5)

    print(uf.connected(0, 2))  # Output: True
    print(uf.connected(3, 5))  # Output: True
    print(uf.connected(2, 4))  # Output: False

    # Add more edges
    uf.union(2, 4)

    print(uf.connected(2, 4))  # Output: True


dynamic_connectivity_example()


class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


def kruskal(n, edges):
    uf = UnionFind(n)
    mst = []

    # Sort edges by weight
    edges.sort()

    for edge in edges:
        if not uf.connected(edge.u, edge.v):
            uf.union(edge.u, edge.v)
            mst.append(edge)

    return mst


def kruskal_example():
    n = 4  # Number of nodes
    edges = [
        Edge(0, 1, 10),
        Edge(0, 2, 6),
        Edge(0, 3, 5),
        Edge(1, 3, 15),
        Edge(2, 3, 4)
    ]

    mst = kruskal(n, edges)

    print("Edges in MST:")
    for edge in mst:
        print(f"{edge.u} - {edge.v}: {edge.weight}")


kruskal_example()