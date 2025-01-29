def solution(n):
    answer = 0
    samjin = ''
    while n>=1:
        samjin+=str(n%3)
        n = int(n/3)
    print(samjin)
    return sum(int(samjin[i])*3**(len(samjin)-i-1) for i in range(len(samjin)))

