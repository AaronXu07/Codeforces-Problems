n, l = map(int, input().split())

lamps = list(map(int, input().split()))

lamps.sort()

largest = 0

for i in range(1, n):
    dist = lamps[i]-lamps[i-1]
    largest = max(largest, dist)

print(max(largest/2, lamps[0], l-lamps[-1]))