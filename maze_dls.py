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
def dls_maze(maze, start, goal, limit):
    visited = set()
    parent = {}

    def recursive_dls(state, depth):
        visited.add(state)
        print(state)
        if state == goal:
            return True
        if depth == 0:
            return False
        for neighbor in get_neighbors_maze(state, maze):
            if neighbor not in visited:
                parent[neighbor] = state
                if recursive_dls(neighbor, depth - 1):
                    return True
        return False

    print("Order of Nodes Visited:")
    if recursive_dls(start, limit):
        print("Goal Reached")
        path = reconstruct_path(parent, goal, start)
        print_path(path)
    else:
        print("No Goal Found within depth")
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

dls_maze(maze, start, goal,5)
