from unittest import TestCase
from src.dag import Dag


def test_topological_sort_with_two_nodes():
    dag = Dag(2, [[0, 1]])
    assert dag.topological_sort() == [0, 1]


def test_topological_sort_with_three_nodes():
    dag = Dag(3, [[0, 1], [1, 2]])
    assert dag.topological_sort() == [0, 1, 2]
