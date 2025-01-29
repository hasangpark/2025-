from collections import deque
def solution(s):
    dq = deque(s)
    stack = deque()
    while dq:
        if not stack:
            stack.append(dq.popleft())
        else:
            if stack[-1]!=dq[0]:
                stack.append(dq.popleft())
            else:
                dq.popleft()
                stack.pop()
    return 1 if not stack else 0
