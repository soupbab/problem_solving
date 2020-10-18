from itertools import permutations


def n_and_m(n, m):
    numbers = list(range(1, n+1))

    for i in permutations(numbers, m):
        for j in i:
            print(j, end=" ")
        print()


if __name__ == "__main__":
    n, m = map(int, input().split())

    n_and_m(n, m)
