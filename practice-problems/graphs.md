# Graph Practice Problems
1. Draw the undirected graph corresponding to this adjacency matrix:

```
[
    [0,0,0,0,0],
    [0,0,1,1,0],
    [0,1,0,1,1],
    [0,1,1,0,0],
    [0,0,1,0,0],
]
```
2. Draw the undirected graph corresponding to this adjacency list:

```
[
    [5,6],
    [2],
    [1,3],
    [2,5],
    [],
    [0,3,6],
    [0,5],
]
```
3. Draw the directed graph corresponding to this adjacency list:
```
[
    [1,2,3],
    [2,3],
    [3],
    [],
]
```
4. What is the largest number of edges an undirected graph with 8 nodes can have? What if it's directed?
5. True or False: All trees are graphs.
6. True or False: All graphs are trees.
7. Write a Python function `neighbors()` that takes in a graph (adjacency matrix) and a node label, and returns the list of labels of all neighbors of that node. For example, if the adjacency matrix from problem 1 was passed in, and the node 1 was given, the neighbors would be [2,3].