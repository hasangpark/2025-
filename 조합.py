from itertools import combinations
def solution(numbers):
    answer = []
    
    for combi in combinations(numbers,2):
        answer.append(sum(combi))
    return sorted(list(set(answer)))
    
