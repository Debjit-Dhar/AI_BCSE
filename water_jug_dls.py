def get_successors(state, capacity):
    a, b = state
    A, B = capacity
    successors = []

    # Fill A or B
    successors.append((A, b))
    successors.append((a, B))

    # Empty A or B
    successors.append((0, b))
    successors.append((a, 0))

    # Pour A → B
    pour = min(a, B - b)
    successors.append((a - pour, b + pour))

    # Pour B → A
    pour = min(b, A - a)
    successors.append((a + pour, b - pour))

    return successors

def dls_water_jug(start, capacity, goal_amount, depth_limit):
    stack = [(start, 0)]
    parent = {}
    visited = set()

    print(f"For depth {depth_limit}")
    while stack:
        state, depth = stack.pop()

        if state in visited:
            continue
        visited.add(state)

        print(f"Visiting: {state} at depth {depth}")

        if state[0] == goal_amount or state[1] == goal_amount:
            path = reconstruct_path(parent, start, state)
            print("Goal Reached!")
            print("Path:", path)
            return True

        if depth < depth_limit:
            for next_state in get_successors(state, capacity):
                if next_state not in visited:
                    parent[next_state] = state
                    stack.append((next_state, depth + 1))

    print("No goal found within depth limit.")
    return False

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
goal_amount = 4
depth_limit = 5

found = dls_water_jug(start, capacity, goal_amount, depth_limit)
if not found:
    print("Goal not found.")

