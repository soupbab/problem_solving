if __name__ == "__main__":
    n = int(input())
    cards = sorted(list(map(int, input().split())))
    n_array = [0] * 20000001

    for card in cards:
        n_array[card + 10000000] += 1

    m = int(input())
    targets = list(map(int, input().split()))

    for target in targets:
        print(n_array[target + 10000000], end=" ")
