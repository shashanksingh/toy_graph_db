from .graph import Graph
from typing import List
from collections import defaultdict

class Undirected(Graph):
    def __init__(self, number_of_nodes: int, edge_list: List[List[int]]):
        self.edge_list = edge_list
        self.number_of_nodes = number_of_nodes
        self.adjacency_list = defaultdict(list)
        self.ingress_count = defaultdict(int)

    def add_edge(self, from_edge:int, to_edge:int):
        self.adjacency_list[from_edge].append(to_edge)

    def setup_adjacency(self):
        self.adjacency_list = {x:[] for x in range(self.number_of_nodes)}
        for from_edge, to_edge in self.edge_list:
            self.adjacency_list[from_edge] = to_edge
            self.ingress_count[to_edge] += 1
            
    # functionlaties
    def is_it_a_valid_tree(self) -> bool:
        if (
            not self.detect_cycles()
            and len(self.bfs_traversal()) == self.number_of_nodes
        ):
            return True
        return False

    def detect_cycles(self) -> bool:
        pass

    # traversal
    def bfs_traversal(self) -> List[int]:
        pass

    def dfs_traversal(self) -> List[int]:
        pass
