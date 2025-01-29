def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer += str(i)*int(food[i]/2)
    rev_answer=answer[::-1]
    return ''.join(answer+'0'+rev_answer)
