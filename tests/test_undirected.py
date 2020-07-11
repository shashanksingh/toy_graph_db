from src.undirected import Undirected


def test_is_it_a_valid_tree():
    graph = Undirected(5, [[0, 1], [0, 2], [0, 3], [0, 4]])
    assert graph.is_it_a_valid_tree()


def test_is_it_a_valid_tree_with_cycle():
    graph = Undirected(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
    assert not graph.is_it_a_valid_tree()
