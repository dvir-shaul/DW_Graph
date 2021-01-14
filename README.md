![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Directed.svg/1024px-Directed.svg.png)


# Description
This is a project given by Ariel university, the purpose is to implement a directed weighted graph.

# Implementation

The implementation of the graph itself was done by using 3 dictionaries,
A dictionary to keep all nodes, a dictionary to keep the incoming edges from a node 
and the outgoing edges.

We have also created a class for nodes and edges.
Below is the list of the methods and their short summary.
Please look at the code for a more detailed explanation.

![alt text](https://miro.medium.com/max/1027/1*Ud_bNdeWPf4iN1EcydaDFA.png)

# Methods
| DiGraph  | Use | Run time | 
| ------------- | ------------- | --------|
| repr() | prints the graph  | O(V+E) | 
| v_size() | returns amount of nodes  | O(1) | 
| e_size()  | returns amount of edges  | O(1) | 
| get_all_v  | gets the node  | O(1) |
| all_in_edges_of_node | get the edge  | O(1) | 
| all_out_edges_of_node  | add the node to the graph  | O(1) | 
| get_mc  | Content Cell  | O(1) | 
| add_edge  | Get a collection of all nodes  | O(1) | 
| add_node  | Get a collection edges from node  | O(1) | 
| remove_node  | remove a node from the graph  | O(K) | 
| remove_edge  | remove an edge from the graph  | O(1) | 


| Graph_Algo  | Use | Run time | 
| ------------- | ------------- | --------|
| get_graph()  | Returns the graph  | O(1) | 
| load_from_json  | returns a deep copy of the graph | O(V+E) |
| save_to_json | performs one bfs on a given graph  | O(V+E) | 
| shortest_path  | check if the graph is strongly connected  | O(n^2) | 
| connected_component  | returns the shortest path between given nodes.  | O(V+E) | 
| connected_components  | returns a list of the shortest path  | O(V(V+E)) | 
| plot_graph  | Saves the graph in json format  | O(V+E) | 




# Installation
Copy the repository

```bash
git clone
```

# Overview

This project uses varias graph algorithms such as Breadth first search and Dijkstra's algorithm.
More information can be found : 
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

https://en.wikipedia.org/wiki/Breadth-first_search

https://en.wikipedia.org/wiki/Shortest_path_problem



# Test
Use DiGraphTest.py & GraphAlgoTest.py

# Common issues
Check the issues tab for more info.
