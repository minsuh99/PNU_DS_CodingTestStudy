def solution(strings, n):
    return sorted(strings, key=lambda x : (x[n], x))

# 장하의 도움을 받았어여...
