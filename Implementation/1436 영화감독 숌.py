def find_number(number):
    i = 0
    count = 0

    while count != number:
        i += 1

        if "666" in str(i):
            count += 1

    return i


if __name__ == "__main__":
    number = int(input())

    print(find_number(number))
