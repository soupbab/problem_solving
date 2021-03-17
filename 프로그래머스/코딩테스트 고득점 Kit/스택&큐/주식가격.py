def solution(prices):
    answer = [0]
    stack = []

    for price in prices[-2::-1]:
        if not stack or price > stack[-1][0]:
            stack.append((price, 1))
            answer.append(1)
        else:
            count = 0
            while stack and price <= stack[-1][0]:
                count += stack.pop()[1]
            stack.append((price, count + 1))
            answer.append(count + 1)

    answer.reverse()
    return answer
