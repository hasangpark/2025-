def solution(phone_book):
    p_dict = {}
    
    for p in phone_book:
        if p not in p_dict.keys():
            p_dict[p] = 1
            
            
    for p in phone_book:
        now = ''
        for i in range(len(p)):
            now += p[i]
            if now in p_dict.keys():
                p_dict[now]-=1
    
    for pd in p_dict:
        if p_dict[pd]<0:
            return False
    return True
