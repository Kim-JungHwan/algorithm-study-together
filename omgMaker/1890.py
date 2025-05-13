import sys
# ###########################
import io

str_1="""4
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0"""

sys.stdin = io.StringIO(str_1)
# ###########################


# 아래부터는 실제 백준 입력 맞춤
input = sys.stdin.readline

N = int(input())
board = []

for _ in range(N):
    board.append((list(map(int, input().split()))))    

dp = [([0] *  N) for _ in range(N)]

dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            continue
        else:
            jump = board[i][j]
            if i + jump < N:
                dp[i + jump][j] = dp[i + jump][j] + dp[i][j]
            if j + jump < N:
                dp[i][j + jump] = dp[i][j + jump] + dp[i][j]


print(dp[N-1][N-1])          

# for item in dp:
#     print(item)


# def bfs():
#     q = [(0,0)]

#     count = 0

#     while(q):
#         cx, cy = q.pop()

#         if board[cx][cy] == 0:
#             count += 1 
        
#         else:             
#             nx = cx + board[cx][cy]
#             ny = cy
            
#             if nx < N and ny < N:
#                 q.append((nx, ny))

#             nx = cx
#             ny = cy + board[cx][cy]
            
#             if nx < N and ny < N:
#                 q.append((nx, ny))

#     return count

# print(bfs())
