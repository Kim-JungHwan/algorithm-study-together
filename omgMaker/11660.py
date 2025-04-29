import sys
from io import StringIO

# a,b = map(int,sys.stdin.readline().split())

# data = []
# for i in range(a):
#     data.append(list(map(int,sys.stdin.readline().split())))

# targets = []
# for i in range(a):
#     targets.append(list(map(int,sys.stdin.readline().split())))

# 입력 데이터를 문자열로 저장
str_1 ="""4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4"""

sys.stdin = StringIO(str_1)

N, M = map(int, input().split())  # N: 표의 크기, M: 합을 구할 횟수

table1 = [list(map(int, input().split())) for _ in range(N)]


sum_table = [[0] * (N + 1) for _ in range(N + 1)]




# sum_table 계산
for i in range(1, N + 1):
    for j in range(1, N + 1):
        sum_table[i][j] = (table1[i - 1][j - 1]
                            + sum_table[i - 1][j]
                            + sum_table[i][j - 1]
                            - sum_table[i - 1][j - 1])



for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    target = sum_table[x2][y2] - sum_table[x1-1][y2] - sum_table[x2][y1-1] + sum_table[x1-1][y1-1]
    print(target)




