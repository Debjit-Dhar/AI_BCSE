def ibs(start, capacity, goal):
    def get_successors(u):
        """Generate all valid states from the current state u."""
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

        return states

    b = 1
    while True:
        print(f"\nFor Breadth {b}")
        visited = set()
        parent = {}
        l = [start]
        visited.add(start)

        while l:
            u = l.pop(0)
            print(u)

            if u[0] == goal or u[1] == goal:
                print("Goal Reached")
                path = reconstruct_path(parent, u, start)
                print("Path:", path)
                return

            successors = get_successors(u)
            count = 0
            for state in successors:
                if state not in visited:
                    visited.add(state)
                    parent[state] = u
                    l.append(state)
                    count += 1
                    if count == b:
                        break

        b += 1
        if b > 20:  # Avoid infinite loop
            print("No Goal Present within breadth limit")
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
ibs(start, capacity, goal)

