def is_valid(state):
    m_left, c_left, _ = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    if not (0 <= m_left <= 3 and 0 <= c_left <= 3):
        return False
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True

def get_successors(state):
    m, c, b = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    successors = []

    for dm, dc in moves:
        if b == 0:
            new_state = (m - dm, c - dc, 1)
        else:
            new_state = (m + dm, c + dc, 0)

        if is_valid(new_state):
            successors.append(new_state)

    return successors

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
def dls_mc(start, goal, limit):
    visited = set()
    parent = {}

    def recursive_dls(state, depth):
        visited.add(state)
        print(state)
        if state == goal:
            return True
        if depth == 0:
            return False
        for neighbor in get_successors(state):
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
start = (3, 3, 0)
goal = (0, 0, 1)

dls_mc(start, goal, limit=5)
