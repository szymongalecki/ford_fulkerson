class Node:
    # Node constructor
    def __init__(self, id) -> None:
        self.id = id
        self.edges = {}

    # string representation of Node
    def __repr__(self) -> str:
        return f"{self.id} : {self.edges}"

    # add edge with given (id, flow, capacity) to the Node
    def add_edge(self, id, flow, capacity):
        self.edges[id] = [flow, capacity]

    def get_id(self):
        return self.id

    def get_edges(self):
        return self.edges


class Network:
    # Network constructor
    def __init__(self) -> None:
        self.number_of_nodes = 0
        self.nodes = {}
        self.get_input()

    # string representation of Network
    def __repr__(self) -> str:
        res = ""
        for _, node in self.nodes.items():
            res += "\n" + str(node)
        return res

    # parse input
    def get_input(self):
        # number of nodes in the network
        self.number_of_nodes = int(input())

        # skip reading node names as they are not unique
        while input() != "DESTINATIONS":
            pass

        # create all edges
        for _ in range(int(input())):
            from_id, to_id, capacity = [int(_) for _ in input().split()]
            if from_id not in self.nodes.keys():
                node = Node(from_id)
                self.nodes[from_id] = node
            self.nodes[from_id].add_edge(to_id, 0, capacity)

    # Breadth-first search Network traversal
    def BFS(self, from_id, target, path):
        # check if node is in Network
        if not from_id in self.nodes.keys():
            return False

        # mark all vertices as not visited and create queue
        visited = [False] * self.number_of_nodes
        queue = []

        queue.append(from_id)
        visited[from_id] = True

        while not len(queue) == 0:
            from_id = queue.pop(0)
            if from_id in self.nodes.keys():
                for to_id in self.nodes[from_id].get_edges():
                    if visited[to_id] == False and (self.nodes[from_id].get_edges()[to_id][1] > 0 or self.nodes[from_id].get_edges()[to_id][1] == -1):
                        queue.append(to_id)
                        visited[to_id] = True
                        path[to_id] = from_id
        if visited[target]:
            return True
        return False

    def ford_fulkerson(self, from_id, target):
        path = [-1] * self.number_of_nodes
        max_flows = 0
        while self.BFS(from_id, target, path):
            flow = float("Inf")
            start_node = target
            print(path)
            testMe = [start_node]
            while start_node != from_id:
                cap = self.nodes[path[start_node]].get_edges()[start_node][1]
                if cap == -1:
                    cap = float("Inf")
                flow = min(flow, cap) 
                start_node = path[start_node]
                testMe.append(start_node)
            print(testMe)
            max_flows = max_flows + flow
            print(flow)

            #update residual graph
            start_node2 = target
            while(start_node2 != from_id):
                u = path[start_node2]
                self.nodes[u].get_edges()[start_node2][1] = self.nodes[u].get_edges()[start_node2][1] - flow

                # check if node is in Network
                if start_node2 not in self.nodes.keys():
                    node = Node(start_node2)
                    self.nodes[start_node2] = node
                    self.nodes[start_node2].add_edge(u, 0, 0)
                elif not u in self.nodes[start_node2].get_edges():
                    self.nodes[start_node2].add_edge(u, 0, 0)
                self.nodes[start_node2].get_edges()[u][1] = self.nodes[start_node2].get_edges()[u][1] + flow

                start_node2 = u
        print(net)
        return max_flows




# n = Node(10)
# n1 = Node(30)
# n.add_edge(30, 2, 10)
# print(n, n1)
net = Network()
# print(net)
# net.add_nodes(n)
# net.add_nodes(n1)
print(net)
print(f"max flow {net.ford_fulkerson(0, 53)}")
# print(net.BFS(0, 54))
