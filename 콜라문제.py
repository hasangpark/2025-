def solution(a, b, n):
    receive = 0
    rsv=0
    while n>=a:
        receive +=int(n/a)*b
        rsv = n%a
        n = int(n/a)*b+rsv
    return receive
