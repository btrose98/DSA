"""
    Breadth First Search:
    - Explores all neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.
    - Used for:
        > Shortest path finding
        > Network Routing
        > Web crawling
    - Time complexity = O(V+E)

    Steps:
    1. Start at the root:
        - Choose a starting node as the root and mark as visited.

    2. Explore neighbors:
        - Visit all neighbors of the current node.

    3. Enqueue Neighbors:
        - Add all the unvisited neighbors to a queue.

    4. Dequeue:
        - Remove the front node from the queue. This node becomes the current node.

    5. Repeat:
        - repeat steps 2-4 until there are no nodes left in the queue.
"""

from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}
bfs(graph, 'A')
