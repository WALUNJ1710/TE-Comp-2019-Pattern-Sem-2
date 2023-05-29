visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node,end = " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

#Driver Code
print("Enter the number of nodes in the graph :")
num_nodes = int(input())

graph = {}

for i in range(num_nodes):
    print("Enter the numbers for node {i}: ")
    neighbours = input().split()
    graph[str(i)] = neighbours

start_node = input("Enter the start node for Depth First Search")
print("Following is a depth first search")
dfs(visited, graph, start_node)
