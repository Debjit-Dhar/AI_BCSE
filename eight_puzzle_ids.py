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
def ids_8_puzzle(start, goal, max_depth=20):
    for depth in range(max_depth):
        print(f"Depth Limit: {depth}")
        visited = set()
        parent = {}

        def dls(node, limit):
            visited.add(node)
            print(node)
            if node == goal:
                return True
            if limit == 0:
                return False
            for neighbor in get_neighbors(node):
                if neighbor not in visited:
                    parent[neighbor] = node
                    if dls(neighbor, limit - 1):
                        return True
            return False

        if dls(start, depth):
            print("Goal Reached")
            path = reconstruct_path(parent, goal, start)
            print("Path to Goal:")
            for step in path:
                print(step)
            return
    print("No Goal Found within max depth")
# Example usage:
start = (1, 3, 5,
         4, 2, 0,
         7, 8, 6)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

ids_8_puzzle(start, goal)
