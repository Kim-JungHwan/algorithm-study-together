import sys

# # 첫 번째 문자열
# st_1 = "ACAYKP"
st_1 = sys.stdin.readline().strip()

# 두 번째 문자열
# st_2 = "CAPCAK"
st_2 = sys.stdin.readline().strip()

dp = [[0 for j in range(len(st_2)+1)] for i in range(len(st_1)+1)]

for i in range(1, len(st_1)+1):
    for j in range(1, len(st_2)+1):
        if st_1[i-1] == st_2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(st_1)][len(st_2)])

i, j = len(st_1), len(st_2)

path = []

while i > 0 and j > 0:
    if st_1[i-1] == st_2[j-1]:
        path.append(st_1[i-1])
        i = i -1
        j = j - 1
    else:
        if dp[i-1][j] > dp[i][j-1]:
            i = i -1
        else:
            j = j - 1

# print(path)
print(''.join(reversed(path)))