import heapq
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
def a_star_mc(start, goal):
    def heuristic(state):
        return state[0] + state[1]  # total left

    open_list = []
    heapq.heappush(open_list, (heuristic(start), 0, start))
    parent = {}
    cost = {start: 0}
    visited = set()

    print("Order of Nodes Visited:")
    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current in visited:
            continue
        visited.add(current)
        print(current)

        if current == goal:
            print("Goal Reached")
            path = reconstruct_path(parent, current, start)
            print_path(path)
            return

        for neighbor in get_successors(current):
            new_cost = g + 1
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(open_list, (new_cost + heuristic(neighbor), new_cost, neighbor))

    print("No Goal Found")
start = (3, 3, 0)
goal = (0, 0, 1)
a_star_mc(start,goal)
