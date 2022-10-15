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
        if not from_id in self.nodes:
            return False

        # mark all vertices as not visited and create queue
        visited = [False] * self.number_of_nodes
        queue = []

        queue.append(from_id)
        visited[from_id] = True

        while queue:
            from_id = queue.pop(0)
            print(from_id, end=" ")
            if from_id in self.nodes:
                print(f"{self.nodes[from_id].get_edges()=}")
                for to_id in self.nodes[from_id].get_edges():
                    if visited[to_id] == False:
                        queue.append(to_id)
                        visited[to_id] = True
                        path[to_id] = from_id
                        if to_id == target:
                            return True

    def ford_fulkerson(self, from_id, target):
        path = [-1] * self.number_of_nodes
        flow = float("Inf")

        if self.BFS(from_id, target, path):
            while target != from_id:
                print(target)
                target = path[target]
            print(from_id)

            # Probably wrong
            # if self.BFS(from_id, target, path):
            #     while target != from_id:
            #         target = path[target]
            #         flow = min(flow, self.nodes[path[from_id]].get_edges()[target])

            print(from_id)


# n = Node(10)
# n1 = Node(30)
# n.add_edge(30, 2, 10)
# print(n, n1)
net = Network()
# print(net)
# net.add_nodes(n)
# net.add_nodes(n1)
print(net)
net.ford_fulkerson(0, 54)
# print(net.BFS(0, 54))
