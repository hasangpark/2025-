def solution(n):
    answer = [0] * (n + 1)  # DP 테이블 생성
    answer[1] = 1  # 피보나치 초기값 설정

    for i in range(2, n + 1):
        answer[i] = (answer[i - 1] + answer[i - 2]) # 값 갱신 (모듈러 연산 적용)

    return answer[n]%1234567 # n번째 피보나치 수 반환
