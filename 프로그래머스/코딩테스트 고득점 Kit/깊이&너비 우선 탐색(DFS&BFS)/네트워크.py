def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

        
def solution(n, computers):
    parent = list(range(n))
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                union_parent(parent, i, j)
    
    for i in range(n):
        find_parent(parent, i)
    
    return len(set(parent))
