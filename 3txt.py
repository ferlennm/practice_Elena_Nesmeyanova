n = int(input())
strt = list(map(int, input().split()))

distances = [-1] * n
length = n

for i in range(n):
    if strt[i] == 0:
        length = 0
    elif length != n:
        length += 1
    distances[i] = length

length = n

for i in range(n - 1, -1, -1):
    if strt[i] == 0:
        length = 0
    elif length != n:
        length += 1
    if distances[i] > length:
        distances[i] = length

print(" ".join(map(str, distances)))