def solution(clothes):
    answer = 1
    c_dict = {}
    for clo in clothes:
        if clo[1] not in c_dict.keys():
            c_dict[clo[1]] = 1
        else:
            c_dict[clo[1]] +=1
    
    if len(c_dict.keys())==1:
        for c in c_dict.keys():
            if c_dict[c] !=0:
                return c_dict[c]
    for c in c_dict.keys():
        answer*=c_dict[c]+1
        # print(answer)
    return answer-1
