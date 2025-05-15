from collections import deque
import sys
# ###########################
import io

str_1="""7
6
1 2
2 3
1 5
5 2
5 6
4 7"""


sys.stdin = io.StringIO(str_1)
# ###########################

# 입력 처리
n = int(sys.stdin.readline())  # 컴퓨터 수
m = int(sys.stdin.readline())  # 연결 쌍 수

# 인접 리스트 생성
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)  # 무방향 연결

# 방문 체크
visited = [False] * (n + 1)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    count = 0

    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1  # 감염된 컴퓨터 수 (start는 제외)
    
    return count

# 1번 컴퓨터에서 BFS 시작
print(bfs(1))