# Graph

A **tree** is a popular data structure that simulates a hierarchy of values or objects.
A **hierarchy** is an arrangement of things in which a single object is related to several other objects below it.
A tree is a **connected acyclic graph** — every node has an edge to another node, and no cycles exist.

In a tree, the value or object represented at a specific point is called a **node**.
Trees typically have a single root node with zero or more child nodes that could contain subtrees.
Let’s take a deep breath and jump into some terminology.
When a node has connected nodes, the root node is called the **parent**.
You can apply this thinking recursively. A child node may have its own child nodes, which may also contain subtrees.
Each child node has a single parent node. A node without any children is a leaf node.

Trees also have a total height. The level of specific nodes is called a **depth**.

The topmost node in a tree is called the **root node**.
A node directly connected to one or more other nodes is called a **parent node**.
The nodes connected to a parent node are called **child nodes** or **neighbors**.
Nodes connected to the same parent node are called **siblings**.
A connection between two nodes is called an **edge**.

A **path** is a sequence of nodes and edges connecting nodes that are not directly connected.
A node connected to another node by following a path away from the root node is called a **descendent**,
and a node connected to another node by following a path toward the root node is called an **ancestor**.
A node with no children is called a **leaf node**.
The term **degree** is used to describe the number of children a node has; therefore, a leaf node has degree zero.

## Categories of graphs

* *Undirected* graph—No edges are directed. Relationships between two nodes are mutual. As with roads between cities,
  there are roads traveling in both directions.
* *Directed* graph—Edges indicate direction. Relationships between two nodes are explicit. As in a graph representing a
  child of a parent, the child cannot be the parent of its parent.
* *Disconnected* graph—One or more nodes are not connected by any edges. As in a graph representing physical contact
  between continents, some nodes are not connected. Like continents, some are connected by land, and others are
  separated by oceans.
* *Acyclic* graph—A graph that contains no cycles. As with time as we know it, the graph does not loop back to any point
  in the past (yet).
* *Complete* graph—Every node is connected to every other node by an edge. As in the lines of communication in a small
  team, everyone talks to everyone else to collaborate.
* *Complete bipartite* graph—A vertex partition is a grouping of vertices. Given a vertex partition, every node from one
  partition is connected to every node of the other partition with edges. As at a cheese-tasting event, typically, every
  person tastes every type of cheese.
* *Weighted* graph—A graph in which the edges between nodes have a weight. As in the distance between cities, some
  cities
  are farther than others. The connections “weigh” more

## Graph representations

![graph data structure](./graph_data_structure.png)

### Incidence matrix

An incidence matrix uses a matrix in which the height is the number of nodes in the graph and the width
is the number of edges. Each row represents a node’s relationship with a specific edge.
If a node is not connected by a specific edge, the value 0 is stored.
If a node is connected by a specific edge as the receiving node in the case of a directed graph,
the value -1 is stored. If a node is connected by a specific edge as an outgoing node or connected
in an undirected graph, the value 1 is stored. An incidence matrix can be used to represent both
directed and undirected graphs
![graphincidence_matrix](./graph_incidence_matrix.png)

## Links

- [6-006-introduction-to-algorithms-2011-lec14](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec14.pdf)
- [Algorithm definition](http://web.cs.unlv.edu/larmore/Courses/CSC477/bfsDfs.pdf)