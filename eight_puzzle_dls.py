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
def dls_8_puzzle(start, goal, limit):
    def recursive_dls(node, depth):
        visited.add(node)
        print(node)
        if node == goal:
            return True
        if depth == 0:
            return False
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                parent[neighbor] = node
                if recursive_dls(neighbor, depth - 1):
                    return True
        return False

    visited = set()
    parent = {}

    print("Order of Nodes Visited:")
    if recursive_dls(start, limit):
        print("Goal Reached")
        path = reconstruct_path(parent, goal, start)
        print("Path to Goal:")
        for step in path:
            print(step)
    else:
        print("No Goal Present within depth limit")
# Example usage:
start = (1, 3, 5,
         4, 2, 0,
         7, 8, 6)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

dls_8_puzzle(start, goal,5)
