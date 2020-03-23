# Difference between greedy algorithm and dynamic programming
## Greedy Algorithms

      It work in stages, in each stage a decision is made that is good at that point, without bothering about the future. This means that some local best is chosen.              "It assumes local good selection makes global optimal solution".

The two basic properties of optimal greedy algorithms are:

1. Greedy Choice Property:
 This property says that globally optimal solution can obtained by making a locally optimal solution(greedy). The choice made by a greedy algorithm may depend on earlier choices but not on future. It iteratively makes one greedy choice after another and reduces the given problem into a smaller one.
1. Optimal substructure:
 A problem exhibits optimal substructure if an optimal solution to the problem contains optimal solutions to the subproblems. That means we can solve subproblems and build up the solutions to solve larger problems.

### Greedy Applications:

* Sorting: Selection sort, Topological sort
* Priority Queues: Heap sort
* Huffman coding compression algorithm
* Prim's and Kruskal's algorithms
* Sorted Path in Weighted Graph (Dijikstra's)
* Coin change problem
* Job scheduling algorithms


## Dynamic Programming

Dynamic Programming and memoization work together. 
The main difference b/w dynamic programming and divide & conquer 
is that in case of divide & conquer, 
subproblems are independent, were as in 
DP overlap of subproblems occur. 
By using memoization(maintaining a table), 
dp reduces the exponential complexity to polynomial 
complexity for many problems. 

The major components of dp are:

* Recursion: Solves problem recursively.
* Memoization: To store the result of already solved problems.
In General **DP=Recursion + Memoization**

Properties of DP:

* Optimal substructure: an optimal solution to a problem contains optimal solutions to subproblems.
* Overlapping subproblems: a recursive solution contains a small number of distinct subproblems repeated many a times.


### Dynamic Applications: (Quite extensive applications it has)

* Operations research
* Decision making
* Query optimization
* Water resource engineering
* Economics
* Reservoir Operations problems
* Connected speech recognition
* Slope stability analysis
* Using Matlab
* Using Excel
* Unit commitment
* Image processing
* Optimal Inventory control
* Reservoir operational Problems
* Sap Abap
* Sequence Alignment
* Simulation for sewer management
* Finance
* Production Optimization
* Genetic Algorithms for permutation problem
* Haskell
* HTML
* Healthcare
* Hydro power scheduling
* LISP
* Linear space
* XML indexing and querying
* Business
* Bioinformatics