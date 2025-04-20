import heapq

def heuristic(state, goal):
    """Heuristic: Minimum difference from goal in either jug."""
    return min(abs(state[0] - goal), abs(state[1] - goal))

def get_successors(u, capacity):
    """Generate all possible next states."""
    successors = []

    # Fill Jug A or B
    successors.append((capacity[0], u[1]))
    successors.append((u[0], capacity[1]))

    # Empty Jug A or B
    successors.append((0, u[1]))
    successors.append((u[0], 0))

    # Pour A -> B
    pour = min(u[0], capacity[1] - u[1])
    successors.append((u[0] - pour, u[1] + pour))

    # Pour B -> A
    pour = min(u[1], capacity[0] - u[0])
    successors.append((u[0] + pour, u[1] - pour))

    return successors

def astar_water_jug(start, capacity, goal):
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), 0, start))
    visited = set()
    parent = {}
    g_score = {start: 0}

    while pq:
        f, g, u = heapq.heappop(pq)

        print(f"Visiting {u} with cost {g}")
        visited.add(u)

        if u[0] == goal or u[1] == goal:
            print("Goal Reached!")
            path = reconstruct_path(parent, start, u)
            print("Path:", path)
            return

        for v in get_successors(u, capacity):
            if v not in visited:
                temp_g = g + 1
                if v not in g_score or temp_g < g_score[v]:
                    g_score[v] = temp_g
                    f_score = temp_g + heuristic(v, goal)
                    heapq.heappush(pq, (f_score, temp_g, v))
                    parent[v] = u

    print("No solution found.")

def reconstruct_path(parent, start, goal):
    path = [goal]
    while goal in parent:
        goal = parent[goal]
        path.append(goal)
    path.reverse()
    return path

# Driver
start = (0, 0)
capacity = (3, 5)
goal = 4

print("Order of Nodes visited:")
astar_water_jug(start, capacity, goal)

