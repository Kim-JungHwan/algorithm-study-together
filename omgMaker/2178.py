import sys

# 테스트
# ###########################
import io

# # str_1="""4 6
# # 101111
# # 101010
# # 101011
# # 111011"""

# str_1="""4 6
# 110110
# 110110
# 111111
# 111101"""

str_1="""2 25
1011101110111011101110111
1110111011101110111011101"""

# str_1="""7 7
# 1011111
# 1110001
# 1000001
# 1000001
# 1000001
# 1000001
# 1111111"""

sys.stdin = io.StringIO(str_1)
# ###########################


# 아래부터는 실제 백준 입력 맞춤
input = sys.stdin.readline

def bfs(sx, sy, ex, ey):
    global N, M
    global table1

    q = []
    visited = [[0] * M for _ in range(N)]
    visited[sx][sy] = 1

    q.append((sx, sy))

    while q:
        cx, cy = q.pop(0)

        if (cx, cy) == (ex, ey):
            return visited[cx][cy]

        for dx, dy in ((-1,0), (0, 1), (1,0), (0, -1)):
            nx = cx + dx
            ny = cy + dy

            if 0<=nx<N and 0<=ny<M and table1[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))

N, M = map(int, input().split())  # N: 표의 크기, M: 합을 구할 횟수

table1 = [list(map(int, input().strip())) for _ in range(N)]

ans = bfs(0, 0, N-1, M-1)
print(ans)