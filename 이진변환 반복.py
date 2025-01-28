def solution(s):
    answer = [0,0]
    transform = 0
    remove = 0
    remove += s.count('0')
    s = s.replace('0','')
    transform+=1
    s= bin(len(s))[2:]    
    while s!='1':
        remove += s.count('0')
        s = s.replace('0','')
        transform+=1
        s= bin(len(s))[2:]   
    answer[0] += transform
    answer[1]+=remove
    return answer
        
        
