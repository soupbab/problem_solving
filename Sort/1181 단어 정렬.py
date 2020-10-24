import sys

if __name__ == "__main__":
    n = int(input())
    words = set()

    for _ in range(n):
        words.add(sys.stdin.readline().rstrip())

    words = list(words)
    words.sort()
    words.sort(key=lambda word: len(word))

    for i in words:
        print(i)
