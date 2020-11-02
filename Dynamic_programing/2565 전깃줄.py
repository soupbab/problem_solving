# n = int(input())
# wires = []
# for _ in range(n):
#     wires.append(list(map(int, input().split())))
#
# count = 0
#
# while True:
#     overlaps = [0] * len(wires)
#
#     for i in range(len(wires)):
#         for j in range(i + 1, len(wires)):
#             if wires[i][0] > wires[j][0] and wires[i][1] < wires[j][1]:
#                 overlaps[i] += 1
#                 overlaps[j] += 1
#
#             if wires[i][0] < wires[j][0] and wires[i][1] > wires[j][1]:
#                 overlaps[i] += 1
#                 overlaps[j] += 1
#
#     if sum(overlaps) == 0:
#         break
#
#     wires.pop(overlaps.index(max(overlaps)))
#     count += 1
#
# print(count)

########################################################################################################################

n = int(input())
wires = []
for _ in range(n):
    wires.append(list(map(int, input().split())))

wires.sort(key=lambda x: x[0])

dp = [1] * n

for i in range(n):
    for j in range(i):
        if wires[i][1] > wires[j][1] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1

print(n - max(dp))
