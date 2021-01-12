from GraphInterface import GraphInteface


class DiGraph(GraphInteface):
    """This abstract class represents an interface of a graph."""

    def __init__(self):
        self.mode_changes = 0
        self.nodes_on_graph = 0
        self.edges_on_graph = 0
        self.nodes = {}
        self.edges_in = {}
        self.edges_out = {}

    def __repr__(self):
        lines = 'Nodes: {'
        for key in self.nodes:
            lines += ' ' + str(key) + ' ,'
        lines += ' }\n'

        lines += 'EdgesOut: {'
        for key, value in self.edges_out.items():
            print('key ' + str(key))
            print('value' + str(value))

            lines += ' ' + str(key) + ' : '
            for neighbour in self.edges_out[key]:
                lines += ' ' + str(neighbour) + ' ,'
        lines += ' } '

        return lines

    def get_nodes(self, id1: int) -> dict:
        return self.nodes[id1]

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return self.nodes_on_graph

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.edges_on_graph

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph,
        each node is represented using a pair  (key, node_data)"""
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
         """
        return self.edges_in[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
        weight)
        """
        return self.edges_out[id1]

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mode_changes

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """

        if id1 not in self.nodes or id2 not in self.nodes or weight<0 or id1==id2:
            return False
        try:
            self.edges_out[id1][id2]
            return False
        except:
            e = Edge(id1, id2, weight)
            self.edges_out[id1].update({id2: e})
            self.edges_in[id2].update({id1: e})
            self.edges_on_graph += 1
            self.mode_changes += 1
            return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        if node_id not in self.nodes.keys():
            n = Node(node_id, 0.0, False, -1, pos)
            self.edges_out[node_id] = {}
            self.edges_in[node_id] = {}
            self.nodes[node_id] = n
            self.mode_changes += 1
            self.nodes_on_graph += 1  # self.nodesOnGraph +1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """

        if node_id in self.nodes:
            for key in self.edges_out:  # Go over keys
                try:
                    self.remove_edge(node_id, key)
                    self.remove_edge(key, node_id)
                except KeyError:
                    pass  # If you can't find the key just keep goin

            del self.edges_out[node_id]
            del self.edges_in[node_id]
            del self.nodes[node_id]
            self.nodes_on_graph -= 1
            self.mode_changes += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        try:
            self.edges_out[node_id1][node_id2]  # Check if we Have key , If we don't we get Key Error.
            del self.edges_out[node_id1][node_id2]
            del self.edges_in[node_id2][node_id1]
            self.mode_changes += 1
            self.edges_on_graph -= 1
            return True

        except KeyError:
            return False

  # def __eq__(self, other):
   #     if len(self.nodes) != len(other.nodes):
    #        return False
     #   if len(self.edges_out) != len(other.edges_out):
      #      return False
       # for node in self.nodes:
        #    if not other.nodes.__contains__(node):
         #       return False
        #for edge in self.edges_out:
         #   if not other.edges_out.__contains__(edge):
          #      return False
        #return True

    """data structure to store graph edges"""


class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __repr__(self):
        return repr('[src : ' + str(self.src) + ' dest : ' + str(self.dest) + ' Weight : ' + str(self.weight) + ' ] ')

    """ data structure for adjacency list node"""


class Node:
    def __init__(self, node_id, distance, visited, parent, position):
        self.node_id = node_id
        self.distance = distance
        self.visited = visited
        self.parent = parent
        self.position = position

    def __lt__(self, other):
        return self.distance < other.distance
    def __gt__(self, other):
        return self.distance > other.distance

    def __eq__(self, other):
        return self.distance == other.distance

    def __repr__(self):
        return repr('Key : ' + str(self.node_id))
