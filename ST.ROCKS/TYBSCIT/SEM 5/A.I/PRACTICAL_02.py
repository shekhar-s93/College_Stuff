graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

def bfs(start):
    queue = [start]
    levels = {}
    levels[start] = 0
    visited = set([start])

    while queue:
        node = queue.pop(0)
        neighbours = graph[node]
        for neighbor in neighbours:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                levels[neighbor] = levels[node] + 1

    print("Name: SHKHEAR SUMAN")
    print("Roll No: 48")    
    print("Node Levels (BFS):", levels)
    return visited

print("BFS Traversal Nodes:", str(bfs('A')))

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in graph[vertex] - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))

result = list(bfs_paths(graph, 'A', 'F'))
print("All BFS Paths from A to F:", result)

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

result1 = shortest_path(graph, 'A', 'F')
print("Shortest Path from A to F:", result1)
