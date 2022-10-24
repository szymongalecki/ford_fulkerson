import sys
# number of nodes in the network
number_of_nodes = int(input())
graph = [[0 for x in range(number_of_nodes)] for y in range(number_of_nodes)]
# skip reading node names as they are not unique
while input() != "DESTINATIONS":
    pass
# create all edges
for _ in range(int(input())):
    from_id, to_id, capacity = [int(_) for _ in input().split()]
    if capacity == -1:
        capacity = sys.maxsize
    graph[from_id][to_id] = capacity
    graph[to_id][from_id] = capacity

org_graph = [i[:] for i in graph]
# Breadth-first search Network traversal
def BFS(from_id, target, path):

    # mark all vertices as not visited and create queue
    visited = [False] * number_of_nodes
    queue = []

    queue.append(from_id)
    visited[from_id] = True

    while not len(queue) == 0:
        from_id = queue.pop(0)
        for to_id in range(len(graph[from_id])):
            if visited[to_id] == False and graph[from_id][to_id] > 0:
                queue.append(to_id)
                visited[to_id] = True
                path[to_id] = from_id
                if visited[target]:
                    return True
    return False

def ford_fulkerson(from_id, target):
    path = [-1] * number_of_nodes
    max_flows = 0
    while BFS(from_id, target, path):
        flow = sys.maxsize
        start_node = target
        print(path)
        while start_node != from_id:
            flow = min(flow, graph[path[start_node]][start_node]) 
            start_node = path[start_node]
        max_flows = max_flows + flow

        #update residual graph
        start_node2 = target
        while(start_node2 != from_id):
            u = path[start_node2]
            graph[u][start_node2]= graph[u][start_node2] - flow
            graph[start_node2][u] = graph[start_node2][u] + flow
            start_node2 = u

    return max_flows

# Function for Depth first search
# Traversal of the graph
def dfs(graph, s, visited):
    visited[s] = True
    for v in range(len(graph)):
        # If there is an edge and we haven't visited
        if graph[s][v] > 0 and not visited[v]:
            # Call recusively from new vertex
            dfs(graph, v, visited)

def min_cut(source):
    if not org_graph:
        return False

    edges = []

    # Perform DFS
    visited = [False] * len(graph)
    dfs(graph, source, visited)

    # Check for edges that had a capacity in the original graph, but
    # now has 0 capacity.
    # Also has to go from visited in the DFS to not visited
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 0 and org_graph[i][j] > 0 and visited[i] and not visited[j]:
                edges.append((i, j, org_graph[i][j]))

    return edges


print(f"Max flow: {ford_fulkerson(0,54)}")
print(f"Min cut: {min_cut(0)}")

