def solution(k, score):
    answer = []
    fame = []
    for i in range(len(score)):
        if i<k:
            fame.append(score[i])
            fame = sorted(fame,reverse=True)
            answer.append(fame[i])
        else:
            fame.append(score[i])
            fame = sorted(fame,reverse=True)
            answer.append(fame[k-1])
    return answer
