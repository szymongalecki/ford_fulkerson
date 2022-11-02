"""
run it:
    cat input.txt | python3 ff.py
"""


def parse_input():
    # number of nodes in the network
    node_count = int(input())
    graph = [[0 for _ in range(node_count)] for _ in range(node_count)]

    # skip reading node names as they are not unique
    while input() != "DESTINATIONS":
        pass

    # for each connection create two edges with equal capacities
    for _ in range(int(input())):
        from_, to_, capacity = [int(_) for _ in input().split()]
        if capacity == -1:
            capacity = float("inf")
        graph[from_][to_] = capacity
        graph[to_][from_] = capacity

    # original graph
    original_graph = [i[:] for i in graph]
    return graph, original_graph, node_count


# Breadth-first search Network traversal
def bfs(from_, target, path):
    # mark all vertices as not visited and create queue
    visited = [False] * node_count
    queue = [from_]
    visited[from_] = True

    while queue:
        from_ = queue.pop(0)
        for to_, _ in enumerate(graph[from_]):
            if not visited[to_] and graph[from_][to_] > 0:
                queue.append(to_)
                visited[to_] = True
                path[to_] = from_
                if visited[target]:
                    return True
    return False


def ford_fulkerson(from_, target):
    path = [-1] * node_count
    max_flow = 0
    while bfs(from_, target, path):
        flow = float("inf")
        current = target

        while current != from_:
            flow = min(flow, graph[path[current]][current])
            current = path[current]
        max_flow += flow

        # update residual graph
        current = target
        while current != from_:
            prev = path[current]
            graph[prev][current] -= flow
            graph[current][prev] += flow
            current = prev
    return max_flow


# Depth-First search taversal
def dfs(graph, s, visited):
    visited[s] = True
    for v, _ in enumerate(graph):
        # if there is an edge and we haven't visited
        if graph[s][v] > 0 and not visited[v]:
            # call recusively from new vertex
            dfs(graph, v, visited)


def min_cut(source):
    # perform DFS
    edges = []
    visited = [False] * len(graph)
    dfs(graph, source, visited)

    # search for edges that had a positive capacity in the original graph,
    # but now have 0 capacity,
    # additionally those edges have to go from visited in the DFS to not visited
    for i, _ in enumerate(graph):
        for j, _ in enumerate(graph):
            if (
                graph[i][j] == 0
                and original_graph[i][j] > 0
                and visited[i]
                and not visited[j]
            ):
                edges.append((i, j, original_graph[i][j]))
                # edges.append(f"{i}->{j}, f={original_graph[i][j]}")
    return edges


graph, original_graph, node_count = parse_input()
print(f"Max flow: {ford_fulkerson(0,54)}")
print(f"Min cut: {min_cut(0)}")
