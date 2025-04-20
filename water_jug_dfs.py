def dfs(start, capacity, goal):
    stack = [start]  # Use stack for DFS
    visited = set()
    parent = {}
    visited.add(start)

    print(start)

    while stack:
        u = stack.pop()
        if u[0] == goal or u[1] == goal:
            print(u)
            print("Goal Reached")
            path = reconstruct_path(parent, u, start)
            print("Path:", path)
            return

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
                stack.append(state)
                parent[state] = u
                visited.add(state)  # Mark as visited when added to stack (to avoid duplicates)
                print(state)

    print("No Goal Present")


def reconstruct_path(parent, goal, start):
    path = [goal]
    while goal in parent:
        goal = parent[goal]
        path.append(goal)
    path.reverse()
    return path


# Driver code
start = (0, 0)
capacity = (3, 5)
goal = 4

print("Order of Nodes Visited:")
dfs(start, capacity, goal)

