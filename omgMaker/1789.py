import sys

input = sys.stdin.readline

S = int(input())

arr = []

sum = 0

i = 1

while(1):
    target = sum + i
    if (target < S):
        arr.append(i)
        sum += i
    elif(target == S):
        arr.append(i)
        break
    else:
        arr.pop()
        arr.append(S-sum)
        break
    i += 1

print(len(arr))