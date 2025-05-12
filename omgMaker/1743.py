import sys
# ###########################
import io

str_1="""3 4 5
3 2
2 2
3 1
2 3
1 1"""


sys.stdin = io.StringIO(str_1)
# ###########################


# 아래부터는 실제 백준 입력 맞춤
input = sys.stdin.readline

N, M, K = map(int, input().split()) # N = 세로, M = 가로

graph = [[0 for _ in range(M+1)] for _ in range(N+1)]


maxNUm = 0

for _ in range(K):
    X, Y = map(int, input().split())
    graph[X][Y] = 1

def dfs(row, col):
    global graph

    dxdy = [[1,0], [-1,0], [0, 1], [0, -1]]
    graph[row][col] = 0
    count = 1

    stack = [(row, col)]
    
    while(stack):
        cx, cy = stack.pop()

        for item in dxdy:
            nx = cx + item[0]
            ny = cy + item[1]

            if 1 <= nx <= N and 1 <= ny <= M and graph[nx][ny] == 1:
                count += 1
                stack.append([nx, ny])
                graph[nx][ny] = 0
            
    return count
            

for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == 1:
            maxNUm = max(maxNUm, dfs(i, j))

print(maxNUm)
