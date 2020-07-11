from .graph import Graph
from collections import defaultdict
from typing import List

# Top Sort: https://www.youtube.com/watch?v=dis_c84ejhQ
# Top Sort: https://www.cs.usfca.edu/~galles/visualization/TopoSortDFS.html


class Dag(Graph):
    def __init__(self, number_of_nodes: int, edge_list: List[List[int]]):
        self.adjacency_list = defaultdict(list)
        self.ingress_count = defaultdict(int)
        self.number_of_nodes = number_of_nodes
        self.edge_list = edge_list
        # TODO : validation

    def add_edge(self, from_edge: int, to_edge: int):
        self.adjacency_list[from_edge].append(to_edge)

    def setup_adjacency_list(self):
        self.adjacency_list = {
            label_of_node: [] for label_of_node in range(self.number_of_nodes)
        }
        for edge_from, edge_to in self.edge_list:
            self.adjacency_list[edge_from].append(edge_to)
            self.ingress_count[edge_to] += 1

    def topological_sort(self) -> List:
        topological_sort = []
        self.setup_adjacency_list()
        no_ingress_node = [
            node
            for node in range(self.number_of_nodes)
            if node not in self.ingress_count
        ]

        while no_ingress_node:
            element = no_ingress_node.pop()
            topological_sort.append(element)

            for connected_node in self.adjacency_list[element]:
                self.ingress_count[connected_node] -= 1
                if self.ingress_count[connected_node] == 0:
                    no_ingress_node.append(connected_node)
        if len(topological_sort) != self.number_of_nodes:
            return []  # cycles
        else:
            return topological_sort  # why no reversed ?

    def is_topological_sort_possible(self):
        return self.topological_sort() != []
