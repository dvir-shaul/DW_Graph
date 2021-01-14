import heapq
import math
import random
import sys
import json
import datetime

import GraphInterface
from DiGraph import DiGraph
from DiGraph import Edge
from DiGraph import Node
from GraphInterface import GraphInteface

from GraphAlgoInterface import GraphAlgoInterface
from typing import List
import matplotlib.pyplot as plt
import numpy as np


class GraphAlgo(GraphAlgoInterface):
    """This abstract class represents an interface of a graph."""
    dw_graph = DiGraph()


    def __init__(self, graph: DiGraph = None):
        self.dw_graph = graph
        self.d=0

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.dw_graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """

        try:
            with open(file_name, "r") as f:
                dict_graph = json.load(f)
                dw_graph1 = DiGraph()
                for nodes in dict_graph["Nodes"]:
                    try:
                        position = (nodes["pos"]).split(",")  # Give a string of the position
                        pos_tuple = tuple(float(i) for i in position)
                        id = nodes["id"]  # Give a the node id
                        dw_graph1.add_node(id, pos_tuple)
                    except KeyError:
                        id = nodes["id"]  # Give a the node id
                        dw_graph1.add_node(id, None)

                for edges in dict_graph["Edges"]:
                    src = edges["src"]
                    weight = edges["w"]
                    dest = edges["dest"]
                    dw_graph1.add_edge(src, dest, weight)

                self.dw_graph = dw_graph1
                return True

        except IOError as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """
        nodes = []
        edges = []
        for k, v in self.dw_graph.get_all_v().items():
            k1 = self.dw_graph.get_nodes(k)
            a_node = {"pos": k1.position, "id": k}
            nodes.append(a_node)
            for edge in self.dw_graph.all_out_edges_of_node(k).values():
                an_edge = {"src": edge.src, "w": edge.weight, "dest": edge.dest}
                edges.append(an_edge)
        new_graph = {"Edges": edges, "Nodes": nodes}
        try:
            with open(file_name, "w") as f:
                json.dump(new_graph, indent=4, fp=f)
            return True

        except Exception as e:
            print(e)
        return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        We set the distance to be inf for all nodes except the start node.
        We iterate over the graph and update each nodes distance .
        O(V+E)

        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, the path as a list
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """

        if id1 == id2:
            return 0, [id1]
        if id1 not in self.dw_graph.nodes or id2 not in self.dw_graph.nodes:
            return math.inf, []

        for n in self.dw_graph.get_all_v().values():  # Set all distance to be max value.
            if n.node_id != id1:
                n.distance = sys.maxsize
                n.visited = 0
        path = []
        min_heap=[]
        self.dw_graph.nodes[id1].distance = 0
        heapq.heappush(min_heap,(self.dw_graph.nodes[id1].distance,self.dw_graph.nodes[id1]))

        while len(min_heap):
            node = heapq.heappop(min_heap)  # pop the smallest item
            current = node[1]  # Get node from tuples
            current.visited = 1  # Set the node to visited

            for neighbour in self.dw_graph.all_out_edges_of_node(current.node_id).values():  # Get neighbours
                if self.dw_graph.nodes[neighbour.dest].visited == 0:  # if we didn't visit this neighbour
                    new_dist = current.distance + neighbour.weight  # Set new distance

                    if self.dw_graph.nodes[neighbour.dest].distance > new_dist:  # If new distance is smaller , update it.
                        self.dw_graph.nodes[neighbour.dest].distance = new_dist

                        heapq.heappush(min_heap,(self.dw_graph.nodes[neighbour.dest].distance,
                                         self.dw_graph.nodes[neighbour.dest]))  # add to priority queue
                        self.dw_graph.nodes[neighbour.dest].parent = current.node_id  # Update parent

        if self.dw_graph.nodes[id2].distance == sys.maxsize:  # if the distance is still max value , can't reach
            return math.inf, []


        path.append(id2)
        current = self.dw_graph.nodes[id2].parent
        self.dw_graph.nodes[id1].parent=-1
        while current != -1:  # Traverse backwards until parent is -1
            path.append(current)
            current = self.dw_graph.nodes[current].parent
        path.reverse()
        return self.dw_graph.nodes[id2].distance, path

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        For each node in the graph we perform a BFS from that node, then we perform
        BFS only the graph is inverted, the intersection of lists will represent the
        strongly connected component.
        O(V+E)
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        list1 = []
        list2 = []
        if id1 in self.dw_graph.nodes:
            list1 = self.bfs(id1, False)
            list2 = self.bfs(id1, True)

        list3 = []
        temp=set(list2)
        for value in list1 :
            if value in temp:
                list3.append(value)
                self.dw_graph.nodes[value].distance=-10
        list3.sort()
        return list3

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        We iterate over the graph and perform SCC for each node.
        if that node was put in a connected component change its distance to be -10,
        Thus only we encounter a node that has a distance not -10 check for its SCC.
        O(V(V+E))

        @return: The list all SCC
        """
        for n in self.dw_graph.get_all_v().values():
            n.distance=0.0
        mega_list = []
        for n in self.dw_graph.get_all_v().values():
            if n.distance!=-10:
                mega_list.append(self.connected_component(n.node_id))
        return mega_list


    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """

        nodes_on_graph = self.dw_graph.get_all_v()
        for k, v in nodes_on_graph.items():
            if v.position is None:
                x_rand = random.uniform(0.5, self.dw_graph.v_size())
                y_rand = random.uniform(0.5, self.dw_graph.v_size())
                v.position = (x_rand, y_rand)
        x_vals = []
        y_vals = []
        n = list(nodes_on_graph.keys())
        for k, v in nodes_on_graph.items():  # draw nodes
            x_vals.append(v.position[0])
            y_vals.append(v.position[1])

        fig, ax = plt.subplots()
        plt.plot(x_vals, y_vals, 'ro', markersize=5, data="d")

        for p, txt in enumerate(n):
            ax.annotate(n[p], (x_vals[p]+0.00003, y_vals[p]),  color='g')

        for n in nodes_on_graph:
            n1 = self.dw_graph.get_nodes(n)
            x = n1.position[0]
            y = n1.position[1]
            for r in self.dw_graph.all_out_edges_of_node(n):
                dx = self.dw_graph.get_nodes(r).position[0]
                dy = self.dw_graph.get_nodes(r).position[1]
                ax.quiver(x, y, dx-x, dy-y, angles='xy', scale_units='xy', scale=1)
                #plt.arrow(x, y, dx - x, dy - y, head_width=0.0009, width=0.00005, length_includes_head=True)


        plt.xlabel("x axis ")
        plt.ylabel("y axis ")
        plt.title("The title of the graph")
        plt.show()

    def bfs(self, start_node: int, flag: bool) -> bool:
        """
        Performs breathd first search on the graph.
        if flag is set to true we perform BFS as if the graph if inverted.
        Otherwise BFS is run normally.
        """
        for n in self.dw_graph.get_all_v().values():
            n.visited = False
        queue = [self.dw_graph.nodes[start_node]]
        self.dw_graph.nodes[start_node].visited = True
        node_list = [start_node]
        while queue:
            current = queue.pop()
            if not flag:
                for e in self.dw_graph.all_out_edges_of_node(current.node_id).keys():
                    if not self.dw_graph.nodes[e].visited:
                        self.dw_graph.nodes[e].visited = True
                        queue.append(self.dw_graph.nodes[e])
                        node_list.append(e)
            else:
                for e in self.dw_graph.all_in_edges_of_node(current.node_id).keys():
                    if not self.dw_graph.nodes[e].visited:
                        self.dw_graph.nodes[e].visited = True
                        queue.append(self.dw_graph.nodes[e])
                        node_list.append(e)

        return node_list