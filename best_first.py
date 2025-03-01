import heapq

def cal_heuristic(graph):
    heuristic = [float('inf')] * len(graph)
    for i in range(len(graph)):
        non_zero_weights = [graph[i][j] for j in range(len(graph[i])) if graph[i][j] > 0]
        heuristic[i] = min(non_zero_weights) if non_zero_weights else 0
    return heuristic

def best_first(graph, start, goals):
    pq = []  # Priority queue
    parent = {}  # Parent dictionary for path reconstruction
    heuristic = cal_heuristic(graph)
    visited = [False] * len(graph)
    
    heapq.heappush(pq, (heuristic[start], start))  # (heuristic, node)
    
    while pq:
        _, u = heapq.heappop(pq)  # Get the node with the lowest heuristic value
        
        if visited[u]:
            continue  # Skip already visited nodes
        
        visited[u] = True
        print(f"Visiting node {u}")

        if u in goals:
            print("Goal Reached")
            path = reconstruct_path(parent, u, start)
            print("Path:", path)
            return path

        for i in range(len(graph)):
            if graph[u][i] > 0 and not visited[i]:  # Valid neighbor
                heapq.heappush(pq, (heuristic[i], i))  # Push node based on heuristic
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

best_first(graph, start, goals)

