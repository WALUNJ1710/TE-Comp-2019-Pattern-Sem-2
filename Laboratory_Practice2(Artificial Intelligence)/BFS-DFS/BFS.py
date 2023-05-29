visited = []
queue = []

def bfs(visited, graph, node):
    visited.append()
    queue.append()

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

#Driver code
print("Enter the number of nodes in graph")
num_nodes = int(input())

graph = {}
for i in range(num_nodes):
    print("Enter nighbours for node {i}: (seperated by space or press enter)")
    neighbours = input().split()
    graph[str[i]] = neighbours

start_node = input("Enter the start node for Vredth First Search")

print("Following is the Breadth First Search")
bfs(visited, graph, start_node)
