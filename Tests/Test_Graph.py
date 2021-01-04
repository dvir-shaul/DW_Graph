from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def check_di_graph():
    """
        Added Some Tests , basic add/remove nodes, more tests to come

    """

    g = DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(1, 3, 1.9)
    g.add_edge(1, 3, 2.1)
    #g.remove_edge(1,3)
    #g.remove_node(1)
    #g.add_node(1)
    #g.add_edge(1, 2, 1.5)
    print(g.remove_edge(3,5))
    g.remove_node(1)
<<<<<<< HEAD
    g.add_node(1)
    g.add_edge(1, 2, 1.5)
    g.remove_node(2)
    print(g)  # prints the __repr__ (func output)
    #g_algo = GraphAlgo(g)
    #print(g_algo.size())
    #print(g_algo.shortest_path(0, 3))
=======
    print(g.edgesOut)
    print(g.edgesIn, g.get_all_v())
    print(g.all_in_edges_of_node(3))
    print(g.nodesOnGraph, g.get_mc() , g.edgesOnGraph)# prints the __repr__ (func output)
>>>>>>> 4f217407c170f031076d9943114754c647f8b27a
    #print(g.get_all_v())  # prints a dict with all the graph's vertices.
    #print(g.all_in_edges_of_node(1))
    #print(g.all_out_edges_of_node(1))

if __name__ == '__main__':
    check_di_graph()
