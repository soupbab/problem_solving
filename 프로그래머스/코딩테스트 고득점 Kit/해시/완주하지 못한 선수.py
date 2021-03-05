from collections import defaultdict

def solution(participant, completion):
    participant_dict = defaultdict(int)
    
    for p in participant:
        participant_dict[p] += 1
        
    for c in completion:
        participant_dict[c] -= 1
        
    for d in participant_dict:
        if participant_dict[d] == 1:
            return d
