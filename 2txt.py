n = int(input())
street = list(map(int, input().split()))

distances = [-1] * n
distance = n

for i in range(n):
    if street[i] == 0:
        distance = 0
    elif distance != n:
        distance += 1
    distances[i] = distance

distance = n

for i in range(n - 1, -1, -1):
    if street[i] == 0:
        distance = 0
    elif distance != n:
        distance += 1
    if distances[i] > distance:
        distances[i] = distance

print(" ".join(map(str, distances)))