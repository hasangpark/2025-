def solution(numbers):
    # 숫자를 문자열로 변환
    n_list = list(map(str, numbers))
    # 문자열을 반복 비교를 통해 정렬 (큰 숫자가 먼저 오도록)
    n_list.sort(key=lambda x: x*3, reverse=True)
    # 정렬된 리스트를 합쳐 하나의 문자열로 반환
    answer = ''.join(n_list)
    # "000" 같은 경우를 처리하기 위해 int로 변환 후 다시 문자열로 반환
    return str(int(answer))
