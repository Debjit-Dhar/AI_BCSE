def get_neighbors_maze(state, maze):
    rows, cols = len(maze), len(maze[0])
    r, c = state
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    neighbors = []

    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
            neighbors.append((nr, nc))
    return neighbors

def reconstruct_path(parent, goal, start):
    path = [goal]
    while goal in parent:
        goal = parent[goal]
        path.append(goal)
    path.reverse()
    return path

def print_path(path):
    print("Path to Goal:")
    for step in path:
        print(step)
from collections import deque

def bfs_maze(maze, start, goal):
    visited = set()
    queue = deque([start])
    parent = {}

    print("Order of Nodes Visited:")
    visited.add(start)

    while queue:
        current = queue.popleft()
        print(current)

        if current == goal:
            print("Goal Reached")
            path = reconstruct_path(parent, current, start)
            print_path(path)
            return

        for neighbor in get_neighbors_maze(current, maze):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    print("No Goal Found")
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

bfs_maze(maze, start, goal)
