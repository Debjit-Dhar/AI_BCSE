def dls(graph, start, goals, depth):
    parent = {}
    l = []
    visited = [False] * len(graph)
    visited[start] = True
    nv = 1
    u = start
    d = 0
    print('For depth', depth)
    print(u)
    while nv != len(graph):
        if d < depth:
            for i in range(len(graph[0])):
                if graph[u][i] != 0 and not visited[i]:
                    l.append((i, d + 1))
                    parent[i] = u

        if l:
            u, d = l.pop()
            if not visited[u]:
                print(u)
                visited[u] = True
            nv += 1
        else:
            break

        if u in goals:
            pth = reconstruct_path(parent, u, start)
            print("Path:", pth)
            print('Goal Reached')
            return True  # Return True if the goal is found

    return False  # Return False if the goal is not found within the depth limit


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
x=dls(graph, start, goals,2)
if not x:
    print('No goal found')

