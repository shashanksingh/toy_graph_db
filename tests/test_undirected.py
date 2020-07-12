from src.undirected import Undirected


def test_is_it_a_valid_tree():
    graph = Undirected(5, [[0, 1], [0, 2], [0, 3], [0, 4]])
    assert graph.is_tree()


def test_is_it_a_valid_tree_with_cycle():
    graph = Undirected(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
    assert not graph.is_tree()


def test_find_center_with_4_nodes():
    graph = Undirected(4, [[1, 0], [1, 2], [1, 3]])
    assert graph.find_center() == [1]


def test_find_center_with_5_nodes():
    graph = Undirected(5, [[0, 1], [0, 2], [0, 3], [0, 4]])
    assert graph.find_center() == [0]


def test_find_center_with_6_nodes():
    graph = Undirected(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
    assert graph.find_center() == [3, 4]


def test_number_of_components_with_5_nodes():
    graph = Undirected(5, [[0, 1], [1, 2], [3, 4]])
    assert graph.number_of_components() == 2


def test_number_of_components_with_1_node():
    graph = Undirected(1, [])
    assert graph.number_of_components() == 1
