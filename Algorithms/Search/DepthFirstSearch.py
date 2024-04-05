"""
    Depth First Search:
    - Starting at the root node, explores as long as possible along each branch before backtracking.
    - Used for:
        > Graph traversal - finds cycles, determines reachability between nodes.
        > Maze solving - useful for when finding any valid path is sufficient.
        > Topology sorting -
        > Finding strongly connected components -
        > Cycle detection -
        > Path finding and routing -
    - Time complexity = O(V+E)
        > V: Vertex visit -
        > E: Edge Visit -

    Steps:
    1. Start at root:
        - choose a root node and mark as visited.

    2. Explore adjacent nodes:
        - Visit an adjacent unvisited node from the current node. If there are multiple adjacent unvisited nodes,
            choose one arbitrarily.

    3. Recursion:
        - Once an adjacent node is visited, recursively apply the same process to explore its adjacent nodes. This
            process continues until there are no unvisited adjacent nodes.

    4. Backtrack:
        - If all adjacent nodes are visited, backtrack to the previous node and explore any unvisited nodes from there.

    5. Repeat:
        - repeat steps 2-4 until all nodes in graph are visited.
"""


def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}
visited = set()
dfs(graph, 'A', visited)
