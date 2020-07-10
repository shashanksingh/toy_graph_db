from src.undirected import Undirected


def test_is_it_a_valid_tree():
    graph = Undirected(2, [[0, 1]])
    assert graph.is_it_a_valid_tree() == True


def test_detect_cycles():
    graph = Undirected(2, [[0, 1]])
    assert graph.detect_cycles() == False
