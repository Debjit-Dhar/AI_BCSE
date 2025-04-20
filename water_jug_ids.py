def ids(start, capacity, goal):
    def dls(u, depth, limit, visited, parent):
        if depth > limit:
            return False

        print(u)
        visited.add(u)

        if u[0] == goal or u[1] == goal:
            print("Goal Reached")
            path = reconstruct_path(parent, u, start)
            print("Path:", path)
            return True

        # Generate all possible next states
        states = [
            (capacity[0], u[1]),  # Fill first jug
            (u[0], capacity[1]),  # Fill second jug
            (0, u[1]),            # Empty first jug
            (u[0], 0),            # Empty second jug
        ]

        # Pour from first to second
        pour_to_second = min(u[0], capacity[1] - u[1])
        states.append((u[0] - pour_to_second, u[1] + pour_to_second))

        # Pour from second to first
        pour_to_first = min(u[1], capacity[0] - u[0])
        states.append((u[0] + pour_to_first, u[1] - pour_to_first))

        for state in states:
            if state not in visited:
                parent[state] = u
                if dls(state, depth + 1, limit, visited, parent):
                    return True

        return False

    depth = 0
    while True:
        print(f"\nTrying depth limit: {depth}")
        visited = set()
        parent = {}
        if dls(start, 0, depth, visited, parent):
            return
        depth += 1
        if depth > 50:  # Fail-safe to prevent infinite loops
            print("No Goal Present within depth limit")
            break


def reconstruct_path(parent, goal, start):
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

print("Order of Nodes Visited:")
ids(start, capacity, goal)

