from collections import deque

queue = deque()
queue.appendleft(1)  # puts 1 into the queue
queue.appendleft(2)  # puts 2 into the queue
queue.pop()  # returns 1
queue.pop()  # returns 2








adj_matr = [
    [0,0,1],
    [0,0,0],
    [1,0,0]
]


from collections import deque

def bfs(g, source, target):
    """
    Return True if target is reachable from source in g
    g is an adjacency matrix representation of a graph
    """
    visited = set()
    visited.add(source)
    to_visit = deque()
    to_visit.appendleft(source)

    while len(to_visit) > 0:
        current = to_visit.pop()
        if current == target:
            return True

        neighbors = []
        # get neighbors of current
        for i in range(len(adj_matr[current])):
            if g[current][i] == 1:
                neighbors.append(i)

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                to_visit.appendleft(neighbor)

    return False

print(bfs(adj_matr, 1, 2))
print(bfs(adj_matr, 0, 2))











