from collections import deque
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
def ibs_maze(maze, start, goal, max_breadth=5):
    def limited_bfs(limit):
        visited = set()
        queue = deque([start])
        parent = {}
        visited.add(start)

        print("Order of Nodes Visited:")
        while queue:
            current = queue.popleft()
            print(current)

            if current == goal:
                print("Goal Reached")
                path = reconstruct_path(parent, current, start)
                print_path(path)
                return True

            for neighbor in get_neighbors_maze(current, maze)[:limit]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)
        return False

    for breadth in range(1, max_breadth + 1):
        print(f"\nBreadth Limit: {breadth}")
        if limited_bfs(breadth):
            return

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

ibs_maze(maze, start, goal,100)
