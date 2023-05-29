import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # A utility function to print
    # the constructed MST stored in parent[]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in the shortest path tree
    def minKey(self, key, mstSet):
        # Initialize min value
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V  # Array to store constructed MST
        # Make key 0 so that this vertex is picked as the first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of the MST

        for cout in range(self.V):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in the first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update the distance value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than the new distance and
            # the vertex is not in the shortest path tree
            for v in range(self.V):
                # graph[u][v] is non-zero only for adjacent vertices of u
                # mstSet[v] is False for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if (
                    self.graph[u][v] > 0
                    and mstSet[v] == False
                    and key[v] > self.graph[u][v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

if __name__ == "__main__":
    num_vertices = int(input("Enter the number of vertices: "))
    
    g = Graph(num_vertices)
    
    print("Enter the adjacency matrix (space-separated values).")
    print("Enter '0' for no edge between vertices.")
    
    for i in range(num_vertices):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        g.graph[i] = row
    
    g.primMST()
    
#Enter the number of vertices: 5
#Enter the adjacency matrix (space-separated values).
#Enter '0' for no edge between vertices.
#Enter row 1: 0 2 0 6 0
#Enter row 2: 2 0 3 8 5
#Enter row 3: 0 3 0 0 7
#Enter row 4: 6 8 0 0 9
#Enter row 5: 0 5 7 9 0
