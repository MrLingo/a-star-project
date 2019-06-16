import unittest
import graph_structure as gs
from a_star import AStar
import setup_nodes_and_links as setup

# Necessery instances.
new_graph = gs.Graph()
a_star = AStar()
setup.build_graph(new_graph)

result1 = a_star.search(new_graph, '3', '40')
result2 = a_star.search(new_graph, '3', '70')


class TestAStar(unittest.TestCase):
    def test_search(self):
        self.assertTrue(result1)
        self.assertFalse(result2)
        self.assertRaises(ValueError, a_star.search, new_graph, None, '40')
        self.assertRaises(ValueError, a_star.search, new_graph, 3, '40')
        self.assertRaises(ValueError, a_star.search, 'new_graph', '3', '40')


if __name__ == '__main__':
    unittest.main()
