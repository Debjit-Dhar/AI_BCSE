#Perform BFS upto d where d is the depth cutoff and then perform DFS
def dfs(start,graph,goals,d):
	l=[]
	parent={}
	visited=[False]*len(graph)
	u=start
	dp=0
	l.insert(0,(u,dp))	
	new_l=[]
	while l:
		#print(l)
		u,dp=l.pop()
		if not visited[u]:
			print(u)
			visited[u]=True
			br=0
			for i in range(len(graph)):
				if dp<=d and not visited[i] and graph[u][i]!=0:
					if dp<d:
						l.insert(0,(i,dp+1))
						parent[i]=u
						br+=1
					if dp==d:
						parent[i]=u
						new_l.append(i)					
		if u in goals:
			print('Goal Reached')
			pth=get_path(start,parent,u)
			print(pth)
			return True
	l=new_l
	while l:
		#print(l)
		u=l.pop()
		if not visited[u]:
			print(u)
			visited[u]=True
			br=0
			for i in range(len(graph)):
				if not visited[i] and graph[u][i]!=0:
					l.append(i)
					parent[i]=u
					br+=1
										
		if u in goals:
			print('Goal Reached')
			pth=get_path(start,parent,u)
			print(pth)
			return True
	
	print('No Goal Found')
	return False
def get_path(start,parent,goal):
	pth=[]
	while(goal!=start):
		pth.insert(0,goal)
		goal=parent[goal]
	pth.insert(0,goal)
	return pth
graph = [[0,2,1,0,1,0,0], 
         [2,0,4,8,0,7,0], 
         [1,4,0,0,0,15,0], 
         [0,8,0,0,0,0,0],
         [1,0,0,0,0,0,0],
         [0,7,15,0,0,0,1],
         [0,0,0,0,0,1,0]]

start = 0
goals = [6]
d=1
print("Order of Nodes Visited:")
dfs(start, graph, goals, d)
		
