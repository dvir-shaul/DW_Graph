from DiGraph import DiGraph
from unittest import TestCase
import unittest


class TestDiGraph(TestCase):

    def test_get_nodes(self):
        g = DiGraph()
        g.add_node(0, (23.00, 43))
        self.assertEqual((23.0, 43), g.get_nodes(0).position)

    def test_get_mc(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        self.assertEqual(3, g.get_mc())
        g.remove_node(0)
        self.assertEqual(4, g.get_mc())

    def test_e_size(self):
        g = DiGraph()
        self.assertEqual(0, g.e_size())
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_edge(0, 1, 24)
        self.assertEqual(1, g.e_size())
        g.remove_node(0)
        self.assertEqual(0, g.e_size())
        g.add_edge(0, 1, 0.5)
        self.assertEqual(0, g.e_size())
        g.add_edge(2, 1, 1.5)
        g.add_edge(2, 1, 2.5)
        self.assertEqual(1, g.e_size())

    def test_v_size(self):
        g = DiGraph()
        self.assertEqual(0, g.v_size())
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        self.assertEqual(3, g.v_size())
        g.add_node(3)
        g.add_node(4)
        self.assertEqual(5, g.v_size())
        g.remove_node(0)
        self.assertEqual(4, g.v_size())

    def test_remove_node(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        self.assertEqual(2, g.v_size())
        g.remove_node(0)
        g.remove_node(1)
        self.assertEqual(0, g.v_size())

    def test_remove_edge(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_edge(0, 1, 0.5)
        g.add_edge(0, 2, 1.5)
        self.assertEqual(2, g.e_size())
        g.remove_edge(0, 1)
        self.assertEqual(1, g.e_size())

    def test_e_size(self):
        g = DiGraph()
        self.assertEqual(0, g.e_size())
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_edge(0, 1, 24)
        self.assertEqual(1, g.e_size())
        g.remove_node(0)
        self.assertEqual(0, g.e_size())
        g.add_edge(0, 1, 0.5)
        self.assertEqual(0, g.e_size())
        g.add_edge(2, 1, 1.5)
        g.add_edge(1, 2, 2.5)
        self.assertEqual(2, g.e_size())

    def graph_creator(self, v,e,is_connected,num_of_components,seed):
        g=DiGraph()
        for n in range(v):
            g.add_node(n)
        for i in range(e):
            g.add_edge(i,i+1,0)
            g.add_edge(i+1,i,0)

        return g;

if __name__ == '__main__':
    TestDiGraph()