from .graph import Graph
from typing import List
from collections import defaultdict, deque
from hashlib import md5

MAXIMUM_NUMBER_OF_NODES_THAT_CAN_BE_CENTER = 2
NUMBER_OF_INGRESS_CONNECTION_FOR_LEAVES = 1


class Undirected(Graph):
    def __init__(self, number_of_nodes: int, edge_list: List[List[int]]):
        self.edge_list = edge_list
        self.number_of_nodes = number_of_nodes
        self.adjacency_list = defaultdict(list)
        super()

    def __hash__(self):
        return self.get_class_name() + md5(("").encode("utf-8")).hexdigest()

    def add_edge(self, from_edge: int, to_edge: int):
        self.adjacency_list[from_edge].append(to_edge)
        self.adjacency_list[to_edge].append(from_edge)

    def setup_adjacency(self):
        self.adjacency_list = {x: [] for x in range(self.number_of_nodes)}
        for from_edge, to_edge in self.edge_list:
            self.adjacency_list[from_edge].append(to_edge)
            self.adjacency_list[to_edge].append(from_edge)

    def number_of_components(self):
        pass

    def find_roots_of_minimum_height_tree(self):
        return self.find_center()

    # source : https://www.youtube.com/watch?v=nzF_9bjDzdc
    def find_center(self) -> List[int]:
        if not self.is_tree():
            return []
        if self.number_of_nodes == 1:
            return [0]

        ingress_count = [0] * self.number_of_nodes

        # calculate all ingress
        for edge_to, edge_from in self.edge_list:
            ingress_count[edge_to] += 1
            ingress_count[edge_from] += 1

        leaves = [
            node
            for node in range(self.number_of_nodes)
            if ingress_count[node] <= NUMBER_OF_INGRESS_CONNECTION_FOR_LEAVES
        ]

        count_of_nodes_touches = 0
        while (
            count_of_nodes_touches
            < self.number_of_nodes - MAXIMUM_NUMBER_OF_NODES_THAT_CAN_BE_CENTER
        ):
            # go through all leaves
            # peel them and make ingress for their neibour/kids -= 1
            inner_layer_of_leaves = []
            for leave in leaves:
                for kid in self.adjacency_list[leave]:
                    ingress_count[kid] -= 1
                    if ingress_count[kid] == 1:
                        inner_layer_of_leaves.append(kid)
                ingress_count[leave] = 0
            count_of_nodes_touches += len(leaves)
            leaves = inner_layer_of_leaves
        return leaves

    # source : https://leetcode.com/problems/graph-valid-tree/discuss/382112/easy-peasy-python-solution-comments
    def is_tree(self) -> bool:
        self.setup_adjacency()
        visited = [False] * self.number_of_nodes  # number of nodes
        first_node = 0
        if self.__has_cycles(first_node, visited, parent=-1):
            return False
        return (
            sum(visited) == self.number_of_nodes
        )  # visited all nodes + no cycles is Tree

    # the logic is from https://www.youtube.com/watch?v=vXrv3kruvwE
    def __has_cycles(self, node, visited, parent) -> bool:
        visited[node] = True

        kids = self.adjacency_list[node]
        for kid in kids:
            if (visited[kid] and kid != parent) or (
                not visited[kid]
                and self.__has_cycles(node=kid, visited=visited, parent=node)
            ):
                return True
        return False
