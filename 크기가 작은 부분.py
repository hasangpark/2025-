def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)])<=int(p):
            answer+=1
    return answer
#5/2 =>4  12/1 => 12 7/3 =>5
