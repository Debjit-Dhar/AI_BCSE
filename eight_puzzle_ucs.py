import heapq

def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row, col = divmod(index, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

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

def manhattan_distance(state, goal):
    distance = 0
    for num in range(1, 9):
        idx1 = state.index(num)
        idx2 = goal.index(num)
        x1, y1 = divmod(idx1, 3)
        x2, y2 = divmod(idx2, 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()
def ucs_8_puzzle(start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    visited = set()
    parent = {}
    cost = {start: 0}

    print("Order of Nodes Visited:")

    while open_list:
        current_cost, current = heapq.heappop(open_list)

        if current in visited:
            continue
        visited.add(current)
        print_board(current)

        if current == goal:
            print("Goal Reached")
            path = reconstruct_path(parent, current, start)
            print("Path to Goal:")
            for step in path:
                print_board(step)
            return

        for neighbor in get_neighbors(current):
            new_cost = current_cost + 1  # Each move has uniform cost
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current
                heapq.heappush(open_list, (new_cost, neighbor))

    print("No Goal Found")
start = (1, 3, 5,
         4, 2, 0,
         7, 8, 6)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

ucs_8_puzzle(start, goal)
