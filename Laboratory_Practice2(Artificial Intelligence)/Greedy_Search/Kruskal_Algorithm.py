def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal_mst(edges, num_vertices):
    result = []
    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    parent = list(range(num_vertices))
    rank = [0] * num_vertices

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            result.append((u, v, w))
            union(parent, rank, u, v)

    return result

# Get input from the user
edges = []
num_vertices = int(input("Enter the number of vertices: "))

print("Enter edges (source, destination, weight). Enter 'done' when finished.")

while True:
    edge = input("Edge: ")
    if edge.lower() == "done":
        break
    u, v, w = map(int, edge.split())
    edges.append((u, v, w))

# Find the minimum spanning tree
mst = kruskal_mst(edges, num_vertices)
print("Minimum Spanning Tree:")
print(mst)
#Enter the number of vertices: 5
#Enter edges (source, destination, weight). Enter 'done' when finished.
#Edge: 0 1 4
#Edge: 0 2 1
#Edge: 1 2 2
#Edge: 2 3 4
#Edge: 3 4 3
#Edge: done
#[(0, 2, 1), (1, 2, 2), (3, 4, 3), (2, 3, 4)]

#Enter the number of vertices: 9
#Enter edges (source, destination, weight). Enter 'done' when finished.
#Edge: 0 1 4
#Edge: 0 7 8
#Edge: 1 7 11
#Edge: 1 2 8
#Edge: 2 3 7
#Edge: done
#Minimum Spanning Tree:
#[(0, 1, 4), (2, 3, 7), (0, 7, 8), (1, 2, 8)]
