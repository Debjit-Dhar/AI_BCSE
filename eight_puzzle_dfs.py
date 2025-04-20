def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row, col = divmod(index, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_idx = r * 3 + c
            new_state = list(state)
            new_state[index], new_state[new_idx] = new_state[new_idx], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors

def reconstruct_path(parent, goal, start):
    path = [goal]
    while goal in parent:
        goal = parent[goal]
        path.append(goal)
    path.reverse()
    return path
def dfs_8_puzzle(start, goal):
    stack = [start]
    visited = set()
    parent = {}

    print("Order of Nodes Visited:")

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        print(current)

        if current == goal:
            print("Goal Reached")
            path = reconstruct_path(parent, current, start)
            print("Path to Goal:")
            for step in path:
                print(step)
            return

        for neighbor in reversed(get_neighbors(current)):
            if neighbor not in visited:
                parent[neighbor] = current
                stack.append(neighbor)

    print("No Goal Present")
# Example usage:
start = (1, 3, 5,
         4, 2, 0,
         7, 8, 6)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

dfs_8_puzzle(start, goal)
