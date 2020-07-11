from .graph import Graph
from typing import List
from collections import defaultdict, deque


class Undirected(Graph):
    def __init__(self, number_of_nodes: int, edge_list: List[List[int]]):
        self.edge_list = edge_list
        self.number_of_nodes = number_of_nodes
        self.adjacency_list = defaultdict(list)
        super()

    def add_edge(self, from_edge: int, to_edge: int):
        self.adjacency_list[from_edge].append(to_edge)

    def setup_adjacency(self):
        self.adjacency_list = {x: [] for x in range(self.number_of_nodes)}
        for from_edge, to_edge in self.edge_list:
            self.adjacency_list[from_edge].append(to_edge)
            self.adjacency_list[to_edge].append(from_edge)

    def number_of_components(self):
        pass

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
