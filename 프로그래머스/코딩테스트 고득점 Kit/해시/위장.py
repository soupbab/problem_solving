# from collections import defaultdict
from collections import Counter
from functools import reduce

def solution(clothes):
#     clothes_dict = defaultdict(int)
#     for item, category in clothes:
#         clothes_dict[category] += 1
        
#     answer = 1
#     for count in clothes_dict.values():
#         answer *= count + 1
#     answer -= 1

    counter = Counter([category for item, category in clothes])
    answer = reduce(lambda x, y: x * (y + 1), counter.values(), 1) - 1
    
    return answer
