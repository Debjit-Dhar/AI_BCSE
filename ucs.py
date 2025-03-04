import heapq

def cal_heuristic(graph):
    h = [0] * len(graph)
    
    return h

def fscore(g, h):
    return g + h

def astar(graph, start, goals):
    pq = []
    parent = {}
    visited = set()  # Using a set for efficiency
    g_score = {i: float('inf') for i in range(len(graph))}  # g(n): cost to reach node
    f_score = {i: float('inf') for i in range(len(graph))}  # f(n): estimated total cost

    h = cal_heuristic(graph)
    g_score[start] = 0
    f_score[start] = fscore(0, h[start])

    heapq.heappush(pq, (f_score[start], start))

    while pq:
        _, u = heapq.heappop(pq)

        if u in visited:
            continue

        print(f"Visiting node {u} with cost {g_score[u]}")
        visited.add(u)

        if u in goals:
            print('Goal Reached')
            path_taken = path(parent, start, u)
            print(path_taken)
            return True

        for i in range(len(graph)):
            if graph[u][i] != 0 and i not in visited:
                new_g = g_score[u] + graph[u][i]
                new_f = fscore(new_g, h[i])

                if new_f < f_score[i]:  # Update only if a better path is found
                    g_score[i] = new_g
                    f_score[i] = new_f
                    heapq.heappush(pq, (new_f, i))
                    parent[i] = u  # Store the parent for path reconstruction

    print('No goal found')
    return False

def path(parent, start, goal):
    path = []
    while goal != start:
        path.insert(0, goal)
        goal = parent[goal]
    path.insert(0, goal)
    return path

# Graph Definition
graph = [[0, 2, 1, 0, 1, 0, 0], 
         [2, 0, 4, 8, 0, 7, 0], 
         [1, 4, 0, 0, 0, 15, 0], 
         [0, 8, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 0],
         [0, 7, 15, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 1, 0]]

start = 0
goals = [6]

print('Order of Nodes visited')
astar(graph, start, goals)

