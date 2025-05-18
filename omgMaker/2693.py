import sys


import io


str_1 = """4
1 2 3 4 5 6 7 8 9 1000
338 304 619 95 343 496 489 116 98 127
931 240 986 894 826 640 965 833 136 138
940 955 364 188 133 254 501 122 768 408"""

sys.stdin = io.StringIO(str_1)



input = sys.stdin.readline

T = int(input())

# print(T)

for _ in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-3])
    # print(arr)