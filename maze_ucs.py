import heapq
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
def ucs_maze(maze, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    parent = {}
    cost = {start: 0}
    visited = set()

    print("Order of Nodes Visited:")
    while open_list:
        curr_cost, current = heapq.heappop(open_list)
        if current in visited:
            continue
        visited.add(current)
        print(current)

        if current == goal:
            print("Goal Reached")
            path = reconstruct_path(parent, current, start)
            print_path(path)
            return

        for neighbor in get_neighbors_maze(current, maze):
            new_cost = curr_cost + 1
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(open_list, (new_cost, neighbor))

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

ucs_maze(maze, start, goal)
