import heapq

def get_successors(state, capacity):
    a, b = state
    A, B = capacity
    successors = []

    # Fill Jug A or Jug B
    successors.append(((A, b), 1))  # Fill A
    successors.append(((a, B), 1))  # Fill B

    # Empty Jug A or Jug B
    successors.append(((0, b), 1))  # Empty A
    successors.append(((a, 0), 1))  # Empty B

    # Pour A → B
    pour = min(a, B - b)
    successors.append(((a - pour, b + pour), 1))

    # Pour B → A
    pour = min(b, A - a)
    successors.append(((a + pour, b - pour), 1))

    return successors

def water_jug_ucs(start, capacity, goal):
    pq = []
    parent = {}
    cost_so_far = {}
    visited = set()

    heapq.heappush(pq, (0, start))
    cost_so_far[start] = 0

    while pq:
        current_cost, state = heapq.heappop(pq)

        if state in visited:
            continue

        print(f"Visiting: {state} with cost {current_cost}")
        visited.add(state

        )

        if state[0] == goal or state[1] == goal:
            print("Goal Reached!")
            path = reconstruct_path(parent, start, state)
            print("Path:", path)
            return

        for next_state, cost in get_successors(state, capacity):
            new_cost = current_cost + cost
            if next_state not in cost_so_far or new_cost < cost_so_far[next_state]:
                cost_so_far[next_state] = new_cost
                heapq.heappush(pq, (new_cost, next_state))
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
water_jug_ucs(start, capacity, goal)

