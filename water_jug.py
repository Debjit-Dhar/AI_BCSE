'''Water Jug Problem Solved with BFS'''
def bfs(start, capacity, goal):
    l = []
    visited = set()
    parent = {}  # Dictionary to track the parent of each node
    visited.add(start)
    u = start

    while True:
        print(u)
        states = [
            (capacity[0], u[1]),  # Fill first jug
            (u[0], capacity[1]),  # Fill second jug
            (0, u[1]),            # Empty first jug
            (u[0], 0)             # Empty second jug
        ]

        # Pour water from first jug to second jug
        if u[0] + u[1] > capacity[0]:
            states.append((capacity[0], u[1] - capacity[0] + u[0]))
        else:
            states.append((u[0] + u[1], 0))

        # Pour water from second jug to first jug
        if u[1] + u[0] > capacity[1]:
            states.append((u[0] - capacity[1] + u[1], capacity[1]))
        else:
            states.append((0, u[0] + u[1]))

        for state in states:
            if state in l or state in visited:
                continue
            else:
                l.insert(0, state)
                parent[state] = u  # Track the parent

        if not l:
            break  # If no more states to explore, exit loop

        u = l.pop()
        visited.add(u)

        if u[0] == goal or u[1] == goal:
            print(u)
            print("Goal Reached")
            pth = reconstruct_path(parent, u, start)
            print("Path:", pth)
            return

    print("No Goal Present")


def reconstruct_path(parent, goal, start):
    """Reconstruct the path from goal to start using the parent dictionary."""
    path = [goal]
    while goal in parent:  # Traverse back using the parent dictionary
        goal = parent[goal]
        path.append(goal)
    path.reverse()  # Reverse the path to get start → goal
    return path


start = (0, 0)
capacity = (3, 5)
goal = 4

print("Order of Nodes Visited:")
bfs(start, capacity, goal)
