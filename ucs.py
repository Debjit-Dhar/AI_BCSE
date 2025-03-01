import heapq


def pfunc(h):
    return h 

def ucs(graph, start, goals):
    pq = []  # Priority queue
    g = []  # Stores reached goal nodes
    parent = {}  # Parent dictionary for path reconstruction
    visited = [False] * len(graph)
    
    heapq.heappush(pq, (pfunc(0), (start, 0)))  # (f-score, (node, g-cost))
    
    while pq:
        f_score, (u, cost) = heapq.heappop(pq)  # Get the lowest f-score node
        
        if visited[u]:
            continue  # Skip already visited nodes
        
        visited[u] = True
        print(f"Visiting node {u} with cost {cost}")
        
        if u in goals:
            g.append((u, cost))
            if len(g) == len(goals):  # If all goals are reached
                print("Goal Reached")
                u, cost = min(g, key=lambda x: x[1])  # Get the least cost goal
                path = reconstruct_path(parent, u, start)
                print("Path:", path)
                return path

        for i in range(len(graph)):
            if graph[u][i] > 0 and not visited[i]:  # Valid neighbor
                new_cost = cost + graph[u][i]
                heapq.heappush(pq, (pfunc(new_cost), (i, new_cost)))
                parent[i] = u

def reconstruct_path(parent, goal, start):
    """Reconstructs the path from goal to start using the parent dictionary."""
    path = [goal]
    while goal in parent:
        goal = parent[goal]
        path.append(goal)
    path.reverse()
    return path

graph = [[0,2,1,0,1,0,0], 
         [2,0,4,8,0,7,0], 
         [1,4,0,0,0,15,0], 
         [0,8,0,0,0,0,0],
         [1,0,0,0,0,0,0],
         [0,7,15,0,0,0,1],
         [0,0,0,0,0,1,0]]

start = 0
goals = [6]
ucs(graph, start, goals)

