from unittest import TestCase

from .grid import Grid


class TestGrid(TestCase):
    def test_count_of_connected_components_with_two_island(self):
        a = Grid([[1, 1, 1], [1, 0, 0], [1, 1, 0], [0, 0, 0], [1, 1, 0]])
        assert a.count_of_connected_components() == 2

    def test_count_of_connected_components_with_one_island(self):
        a = Grid([[1, 1, 1], [1, 0, 0], [1, 1, 0]])
        assert a.count_of_connected_components() == 1

    def test_count_of_connected_components_with_zeros_island(self):
        a = Grid([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        assert a.count_of_connected_components() == 0

    def test_dfs(self):
        a = Grid([[1, 1, 1]])
        a.clear_visited()
        a.dfs(0,0)
        assert a.visited == {(0,0),(0,1),(0,2)}

    def test_bfs_with_one_row_grid(self):
        a = Grid([[1, 1, 1]])
        a.clear_visited()
        a.bfs(0, 0)
        assert a.visited == {(0, 0), (0, 1), (0, 2)}

    def test_bfs_with_two_row_grid(self):
        a = Grid([[1, 1, 1],[1, 0, 1]])
        a.clear_visited()
        a.bfs(0, 0)
        assert a.visited == {(0, 1), (1, 2), (0, 0), (1, 1), (1, 0), (0, 2)}
