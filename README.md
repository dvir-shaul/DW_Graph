# Description
The first part of the project is based on a directed weighted graph implementation,

# Methods
| DiGraph  | Use | Run time | 
| ------------- | ------------- | --------|
| v_size() | returns amount of nodes  | O(n^2) | 
| e_size()  | returns amount of edges  | O(n^2) | 
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
| load_from_json  | returns a deep copy of the graph | O(n^2) |
| save_to_json | performs one bfs on a given graph  | O(V+E) | 
| shortest_path  | check if the graph is strongly connected  | O(n^2) | 
| connected_component  | returns the shortest path between given nodes.  | O(V+E) | 
| connected_components  | returns a list of the shortest path  | O(V+E) | 
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