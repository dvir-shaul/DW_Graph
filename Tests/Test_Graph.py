from DiGraph import DiGraph


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
    g.remove_node(1)
    g.add_node(1)
    g.add_edge(1, 2, 1.5)
    g.remove_node(2)
    print(g)  # prints the __repr__ (func output)
    #print(g.get_all_v())  # prints a dict with all the graph's vertices.
    #print(g.all_in_edges_of_node(1))
    #print(g.all_out_edges_of_node(1))

if __name__ == '__main__':
    check_di_graph()
