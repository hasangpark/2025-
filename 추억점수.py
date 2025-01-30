def solution(name, yearning, photo):
    answer = []
    miss_dict = {n:y for n,y in zip(name,yearning)}
    
    for p in photo:
        answer.append(sum(miss_dict[m] for m in p if m in miss_dict.keys()))
    
    return answer
