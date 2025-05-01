import sys
input = sys.stdin.readline

def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end = ' ')

    for next in range(1, N + 1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs():
	global visited, q
	
	while q:
		current = q.pop(0)
		print(current, end = ' ')
		
		for next in range(1, N + 1):
			if not visited[next] and graph[current][next]:
				visited[next] = True
				q.append(next)

N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N + 1)]

for _ in range(M):
    X, Y = map(int, input().split())
    graph[X][Y] = True
    graph[Y][X] = True
	
visited = [False] * (N+1)

dfs(V)
print()

visited = [False] * (N+1)
q = [V]
visited[V] = True

bfs()
print()