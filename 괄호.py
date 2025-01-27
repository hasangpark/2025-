from collections import deque
def solution(s):
    answer = True
    
    dq = deque(s)
    
    cri = 0
    while dq:
        if dq.popleft() == '(':
            cri+=1
        else:
            cri-=1
            if cri<0:
                return False
    return True if cri==0 else False
