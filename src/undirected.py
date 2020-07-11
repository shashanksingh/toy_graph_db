from .graph import Graph
from typing import List
from collections import defaultdict, deque


class Undirected(Graph):
    def __init__(self, number_of_nodes: int, edge_list: List[List[int]]):
        self.edge_list = edge_list
        self.number_of_nodes = number_of_nodes
        self.adjacency_list = defaultdict(list)
        self.ingress_count = defaultdict(int)
        super().__init__()
        
    def add_edge(self, from_edge: int, to_edge: int):
        self.adjacency_list[from_edge].append(to_edge)

    def setup_adjacency(self):
        self.adjacency_list = {x: [] for x in range(self.number_of_nodes)}
        for from_edge, to_edge in self.edge_list:
            self.adjacency_list[from_edge] = to_edge
            self.ingress_count[to_edge] += 1
        # self.sh
    # function-laties
    def is_it_a_valid_tree(self) -> bool:
        return not self.has_cycles()

    def has_cycles(self) -> bool:
        self.setup_adjacency()

        queue = deque()
        count_of_visited_vertices = 0

        for item, value in self.adjacency_list.items():
            if not value:
                queue.append(item)

        while queue:
            node = queue.pop()
            for to_edge in self.adjacency_list[node]:
                self.ingress_count[to_edge] -= 1
                if self.ingress_count[to_edge] == 0:
                    queue.append(to_edge)
            count_of_visited_vertices += 1
        print(count_of_visited_vertices)
        return not (count_of_visited_vertices == self.number_of_nodes)  # True if cycle

    # traversal
    def bfs_traversal(self) -> List[int]:
        pass

    def dfs_traversal(self) -> List[int]:
        pass
