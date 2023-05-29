visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Enter the number of nodes in the graph:")
num_nodes = int(input())

graph = {}
for i in range(num_nodes):
    print(f"Enter the neighbors for node {i}: (separated by space, or press enter for no neighbors)")
    neighbors = input().split()
    graph[str(i)] = neighbors

start_node = input("Enter the start node for Depth-First Search:")

print("Following is the Depth-First Search:")
dfs(visited, graph, start_node)
