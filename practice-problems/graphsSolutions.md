## Solutions
1. ASCII art ahoy!
```
0   1---2 
    | / |
    3   4
```
2. 
```
0----5----3----2----1
|  /
| /
6         4
```
3. This is hard to draw in ASCII, but 
```
      __________
     |    |    |
     |    v    v
0--->1--->2--->3
|    ^    ^    ^
|____|    |    |
|_________|    |
|______________|
```
4. If a graph is undirected, then the most edges it can have is between all pairs of nodes. Suppose our nodes our numbered from 0 to 7. Node 0 can have 7 attached edges, then node 1 can have 6 additional ones (since there's already an edge from 1 to 0), and so on, so the largest possible number of nodes is `1+2+3+4+5+6+7=28`.

A more discrete math-y way to see this is to say that each edge can start at one of 8 nodes and end at one of 7 nodes, so 8*7 = 56 possible edges. However, since this considers the edge from 0 to 1 as different from the edge from 1 to 0, we have to divide by two, again yielding 28.

However, the directed graph case works just like that, but without dividing by two (since 0 -> 1 and 1 -> 0 are different edges!). Another way to get the same result is to do addition but note that each node can have 7 unique outgoing edges, for a total of 7+7+7+7+... = 56 edges.

5. True. Technically, a tree is just a directed graph with no cycles and N-1 edges, where N is the number of nodes -- but I don't expect you to know that definition :)
6. False. Consider a graph with four nodes connected in a square. There is no way to express this as a tree because there is no root (node with no parent).
7. See the `lect26-demo` folder in this very repository!