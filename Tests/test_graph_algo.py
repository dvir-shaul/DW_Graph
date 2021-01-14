import math

from DiGraph import DiGraph
from unittest import TestCase
from GraphAlgo import GraphAlgo


class testGraphAlgo(TestCase):

    def test_load_and_save_from_json1(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        file_name = "g.json"
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_edge(2, 1, 2.5)
        g.add_edge(1, 2, 3.4)
        g.add_edge(0, 1, 2.4)
        g.add_edge(2, 0, 8.4)
        g.add_edge(3, 4, 5.23)
        g.add_edge(4, 3, 8.4)
        # assert for save
        self.assertTrue(ga.save_to_json(file_name))
        # assert for load
        self.assertTrue(ga.load_from_json(file_name))
        # assert for all nodes are the same
        self.assertTrue(g.get_all_v() == ga.get_graph().get_all_v())
        g.remove_node(0)
        self.assertFalse(g.nodes == ga.get_graph().nodes)
        # assert for all changes were the same amount
        self.assertFalse(g.get_mc() == ga.get_graph().get_mc())
        self.assertFalse(g.nodes_on_graph == ga.get_graph().nodes_on_graph)

    def test_connected_component_of_one(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        g.add_node(5)
        self.assertEqual([5], ga.connected_component(5))
        self.assertEqual([[5]], ga.connected_components())

    def test_connected_component(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_edge(2, 1, 2.5)
        g.add_edge(1, 2, 3.4)
        g.add_edge(0, 1, 24)
        g.add_edge(2, 0, 4)
        g.add_edge(3, 4, 5.2)
        g.add_edge(4, 3, 8)
        self.assertEqual([5], ga.connected_component(5))
        self.assertEqual([3, 4], ga.connected_component(3))
        self.assertEqual([0, 1, 2], ga.connected_component(1))
        g.remove_edge(1, 2)
        self.assertEqual([1], ga.connected_component(1))

    def test_connected_components(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        self.assertEqual([[0], [1], [2], [3], [4], [5]], ga.connected_components())
        g.add_edge(2, 1, 2.5)
        g.add_edge(1, 2, 3.4)
        self.assertEqual([[0], [1, 2], [3], [4], [5]], ga.connected_components())
        g.add_node(6)
        g.add_node(7)
        g.add_edge(5, 6, 24)
        g.add_edge(0, 1, 24)
        g.add_edge(6, 5, 24)
        g.add_edge(2, 0, 4)
        g.add_edge(3, 4, 5.2)
        g.add_edge(4, 3, 8)
        g.add_edge(3, 7, 76)
        g.add_edge(5, 3, 5.2)
        g.add_edge(4, 5, 8)
        self.assertEqual([[0, 1, 2], [3, 4, 5, 6], [7]], ga.connected_components())

    def test_shortest_path(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        g.add_node(0)
        self.assertEqual((0, [0]), ga.shortest_path(0, 0))
        g.add_node(1)
        g.add_edge(0, 1, 24)
        self.assertEqual((24, [0, 1]), ga.shortest_path(0, 1))
        g.add_node(2)
        g.add_node(3)
        g.add_edge(1, 2, 3)
        g.add_edge(2, 3, 2.4)
        self.assertEqual((29.4, [0, 1, 2, 3]), ga.shortest_path(0, 3))
        # add shortcut to node 3
        g.add_edge(0, 3, 2.4)
        self.assertEqual((2.4, [0, 3]), ga.shortest_path(0, 3))
        # remove shortcut to node 3
        g.remove_edge(0, 3)
        self.assertEqual((29.4, [0, 1, 2, 3]), ga.shortest_path(0, 3))

    def test_shortest_path_to_null(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        self.assertEqual((math.inf, []), ga.shortest_path(1, 2))

    def test_plot_graph(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_edge(0, 2, 6)
        g.add_edge(0, 1, 4)
        g.add_edge(1, 0, 5)
        g.add_edge(2, 0, 4)
        g.add_edge(3, 4, 5.2)
        g.add_edge(4, 3, 8)
        g.add_edge(0, 5, 5)
        ga.plot_graph()

    def test_plot(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        file_name = "../data/G_10_80_0.json"
        ga.load_from_json(file_name)
        ga.plot_graph()
        file_name = "../data/G_10_80_1.json"
        ga.load_from_json(file_name)
        ga.plot_graph()
        file_name = "../data/G_10_80_2.json"
        ga.load_from_json(file_name)
        ga.plot_graph()


