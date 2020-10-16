# import sys
#
# n = int(sys.stdin.readline().rstrip())
# meetings = []
# for _ in range(n):
#     meetings.append(list(map(int, sys.stdin.readline().rstrip().split())))
#
# now = 0
# cnt = 0
# last_start = max(meetings, key=lambda x: x[0])
# next_meetings = meetings
#
# while now <= last_start[0] and len(next_meetings) > 0:
#     selected = min(next_meetings, key=lambda x: x[1])
#     next_meetings.remove(selected)
#     cnt += 1
#     now = selected[1]
#     next_meetings = list(filter(lambda x: x[0] >= now, next_meetings))
#
# print(cnt)

########################################################################################################################

import sys


def greedy(meetings):
    cnt = 0
    now = 0

    for time in meetings:
        if time[0] >= now:
            now = time[1]
            cnt += 1

    return cnt


if __name__ == "__main__":
    m = int(sys.stdin.readline().rstrip())
    meetings = []
    for _ in range(m):
        meetings.append(list(map(int, sys.stdin.readline().rstrip().split())))

    meetings.sort(key=lambda time: time[0])
    meetings.sort(key=lambda time: time[1])

    print(greedy(meetings))
