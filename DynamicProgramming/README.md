# Dynamic Programming

Dynamic programming (DP) is

* careful brute force  
* divide to subproblems + reuse solution of these subproblems
* subporblems should not have cyclic dependencies

## Memoize

**memoize** - (remember) & re-use solutions to subproblems that help solve problem

The memoized program for a problem is similar to the recursive version with a small modification that it looks into a lookup table before computing solutions. We initialize a lookup array with all initial values as NIL. Whenever we need the solution to a subproblem, we first look into the lookup table. If the precomputed value is there then we return that value, otherwise, we calculate the value and put the result in the lookup table so that it can be reused later.

## bottom-up (Tabulation)

idea of algorithm is start solving program from bottom and go up, may uses in junction with memoize.

The tabulated program for a given problem builds a table in bottom up fashion and returns the last entry from table. For example, for the same Fibonacci number, we first calculate fib(0) then fib(1) then fib(2) then fib(3) and so on. So literally, we are building the solutions of subproblems bottom-up.

## Guessing

try all possible ways of solving subproblem and choose the best one.

## Logical step of using DP

1. define subproblem (for recursion) = find exactly same computation
1. guess (part of solution)
1. topological sort of subproblem dependency DAG
1. build algorithm memoize && (recursive || build DP table bottom-up)
1. try to find ways to save space(memory)
1. solve original problem


## Properties in Dynamic Programming

### Overlapping Subproblems

Like Divide and Conquer, Dynamic Programming combines solutions to sub-problems. Dynamic Programming is mainly used when solutions of same subproblems are needed again and again. In dynamic programming, computed solutions to subproblems are stored in a table so that these don’t have to be recomputed. So Dynamic Programming is not useful when there are no common (overlapping) subproblems because there is no point storing the solutions if they are not needed again. For example, Binary Search doesn’t have common subproblems. If we take an example of following recursive program for Fibonacci Numbers, there are many subproblems which are solved again and again.

# Difference between greedy algorithm and dynamic programming
## Greedy Algorithms

      It work in stages, in each stage a decision is made that is good at that point,
       without bothering about the future. This means that some local best is chosen.              "It assumes local good selection makes global optimal solution".

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