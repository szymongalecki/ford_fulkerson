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
print(graph)

# Breadth-first search Network traversal
def BFS(from_id, target, path):
    # check if node is in Network

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
    print(max_flows)
    while BFS(from_id, target, path):
        flow = sys.maxsize
        start_node = target
        print(path)
        while start_node != from_id:
            flow = min(flow, graph[path[start_node]][start_node]) 
            start_node = path[start_node]
        max_flows = max_flows + flow
        print(flow)

        #update residual graph
        start_node2 = target
        while(start_node2 != from_id):
            u = path[start_node2]
            graph[u][start_node2]= graph[u][start_node2] - flow
            graph[start_node2][u] = graph[start_node2][u] + flow
            start_node2 = u
    return max_flows

print(ford_fulkerson(0,54))