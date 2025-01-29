from itertools import combinations, permutations
def solution(d, budget):
    count = 0
    total = 0
    d = sorted(d)
    for cost in d:
        if total+cost>budget:
            break
        total+=cost
        count+=1
    return count
