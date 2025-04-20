import heapq

def heuristic(state, goal):
    """Heuristic: Greedy estimate of closeness to goal."""
    return min(abs(state[0] - goal), abs(state[1] - goal))

def get_successors(state, capacity):
    """Generate all possible successors (states) from the current state."""
    a, b = state
    A, B = capacity
    successors = set()

    # Fill either jug
    successors.add((A, b))
    successors.add((a, B))

    # Empty either jug
    successors.add((0, b))
    successors.add((a, 0))

    # Pour from A to B
    pour = min(a, B - b)
    successors.add((a - pour, b + pour))

    # Pour from B to A
    pour = min(b, A - a)
    successors.add((a + pour, b - pour))

    return list(successors)

def best_first_water_jug(start, capacity, goal):
    pq = []
    visited = set()
    parent = {}

    # Best-first uses heuristic only
    heapq.heappush(pq, (heuristic(start, goal), start))

    while pq:
        _, state = heapq.heappop(pq)

        if state in visited:
            continue

        print(f"Visiting: {state}")
        visited.add(state)

        if state[0] == goal or state[1] == goal:
            print("Goal Reached!")
            path = reconstruct_path(parent, start, state)
            print("Path:", path)
            return

        for next_state in get_successors(state, capacity):
            if next_state not in visited:
                heapq.heappush(pq, (heuristic(next_state, goal), next_state))
                parent[next_state] = state

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
best_first_water_jug(start, capacity, goal)

