# Dynamic Programming

Dynamic programming (DP) is

* careful brute force  
* divide to subproblems + reuse solution of these subproblems
* subporblems should not have cyclic dependencies

## Memoize

**memoize** - (remember) & re-use solutions to subproblems that help solve problem

## bottom-up

idea of algorithm is start solving program from bottom and go up, may uses in junction with memoize

## Guessing

try all possible ways of solving subproblem and choose the best one.

## Logical step of using DP

1. define subproblem (for recursion) = find exactly same computation
1. guess (part of solution)
1. topological sort of subproblem dependency DAG
1. build algorithm memoize && (recursive || build DP table bottom-up)
1. try to find ways to save space(memory)
1. solve original problem
