from src.undirected import Undirected
from src.dag import Dag
from src.grid import Grid
from src.graph import Graph
from src.tree import Tree


def save_all_graphs_into_storage():
    a = Undirected(2, [[0, 1]])
    b = Dag(2, [[0, 1]])
    c = Grid([[1, 0, 1]])
    d = Graph()
    e = Tree(2, [[0, 1]])

    a.save_into_storage()
    b.save_into_storage()
    c.save_into_storage()
    e.save_into_storage()

    assert a.is_tree()


def test_performance_of_saving_all_graphs_into_storage(benchmark):
    benchmark(save_all_graphs_into_storage)