def solution(cards1, cards2, goal):
    answer = ''
    c1 = []
    c2 = []
    for g in goal:
        if g in cards1:
            c1.append(cards1.index(g))
        elif g in cards2:
            c2.append(cards2.index(g))
        else:
            return "No"
    return "Yes" if c1==[i for i in range(len(c1))] and c2==[i for i in range(len(c2))] else "No"
