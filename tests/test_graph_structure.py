import unittest
import graph_structure as gs
import setup_nodes_and_links as setup

new_graph = gs.Graph()
setup.build_graph(new_graph)
new_node = gs.Node('3', 12)


class TestGraphStructure(unittest.TestCase):
    def test_get_node(self):
        self.assertIsInstance(new_graph.get_node('3'), gs.Node)
        self.assertEqual(new_graph.get_node(3), None)
        self.assertEqual(new_graph.get_node('333'), None)

    def test_get_child_nodes(self):
        self.assertIsInstance(new_node.get_child_nodes, list)
        self.assertIsInstance(new_node.get_links, list)


if __name__ == '__main__':
    unittest.main()
