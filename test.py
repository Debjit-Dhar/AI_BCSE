import heapq
def cal_heuristic(graph):
	h=[float('inf')]*len(graph)
	for i in range(len(graph)):
		for j in range(len(graph)):
			if graph[i][j]!=0 and h[i]>graph[i][j]:
				h[i]=graph[i][j]
	return h
def f(g,h):
	return g+h
def astar(graph,start,goals):
	parent={}
	visited=set()
	pq=[]
	h=cal_heuristic(graph)
	g_score=[float('inf')]*len(graph)
	f_score=[float('inf')]*len(graph)
	g_score[start]=0
	f_score[start]=f(g_score[start],h[start])
	heapq.heappush(pq,(f_score[start],start))
	while pq:
		_,u=heapq.heappop(pq)
		if u in visited:
			continue
		print('Visiting node ',u,' in f cost ',f_score[u])
		visited.add(u)
		if u in goals:
			print('Goal Reached')
			pth=path(parent,start,u)
			print(pth)
			return True
		for i in range(len(graph)):
			if i not in visited and graph[u][i]!=0:
				new_g=g_score[u]+graph[u][i]
				new_f=f(new_g,h[i])
				if new_f<f_score[i]:
					g_score[i]=new_g
					f_score[i]=new_f
					heapq.heappush(pq,(f_score[i],i))
					parent[i]=u
	print('No goal found')
	return False
def path(parent,start,goal):
	pth=[]
	while(goal!=start):
		pth.insert(0,goal)
		goal=parent[goal]
	pth.insert(0,goal)
	return pth

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

				
		
