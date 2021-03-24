def solution(citations):
    answer=0
    citations.sort(reverse=True)
    max_ = citations[0]
    for i in range(max_, -1, -1):
        for index, citation in enumerate(citations):
            if citation >= i and (index + 1) >= i:
                return i
