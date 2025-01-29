def solution(s, n):
    result = ''
    
    for char in s:
        # 대문자일 때 처리
        if char.isupper():
            result += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        # 소문자일 때 처리
        elif char.islower():
            result += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        # 공백이나 기타 문자는 그대로 추가
        else:
            result += char
    
    return result
