def bfs(graph, start, goals):
    l = []
    visited = [False] * len(graph)
    parent = {}  # Dictionary to track the parent of each node
    visited[start] = True
    nv = 1
    u = start
    print(u)
    while nv != len(graph):
        for i in range(len(graph[0])):
            if graph[u][i] != 0 and not visited[i]:
                l.insert(0, i)
                parent[i] = u  # Track the parent
        u = l.pop()
        if not visited[u]:
            nv += 1            
            print(u)
        visited[u] = True
        

        if u in goals:
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


graph = [[0,2,1,0,1,0,0], 
         [2,0,4,8,0,7,0], 
         [1,4,0,0,0,15,0], 
         [0,8,0,0,0,0,0],
         [1,0,0,0,0,0,0],
         [0,7,15,0,0,0,1],
         [0,0,0,0,0,1,0]]

start = 0
goals = [6]
print("Order of Nodes Visited:")
bfs(graph, start, goals)

