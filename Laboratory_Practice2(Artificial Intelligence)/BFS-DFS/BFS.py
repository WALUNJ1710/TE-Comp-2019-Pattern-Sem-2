visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
print("Enter the number of nodes in the graph:")
num_nodes = int(input())

graph = {}
for i in range(num_nodes):
    print(f"Enter the neighbors for node {i}: (separated by space, or press enter for no neighbors)")
    neighbors = input().split()
    graph[str(i)] = neighbors

start_node = input("Enter the start node for Breadth-First Search:")

print("Following is the Breadth-First Search:")
bfs(visited, graph, start_node)
