from collections import deque
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
def ibs_mc(start, goal, max_breadth=5):
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

            for neighbor in get_successors(current)[:limit]:
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
start = (3, 3, 0)
goal = (0, 0, 1)
ibs_mc(start,goal,100)
