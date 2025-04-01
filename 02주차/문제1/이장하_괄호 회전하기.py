# 회전된 s가 올바른 괄호 문자열인지 확인하는 함수
def correct(bracket):
    # 괄호 문자열의 첫 문자가 닫는 괄호이면 올바르지 않음
    if bracket[0] in ["}", "]", ")"]:
        return False

    # 괄호 문자열을 후입선출할 스택 정의
    stack = []
    for b in bracket:
        # 스택이 비어있다면 바로 채움
        if not stack:
            stack.append(b)
        # 현재 문자열이 닫는 괄호이고, 스택의 마지막 괄호가 같은 여는 괄호이면 스택에서 괄호를 삭제함
        elif b == "}" and stack[-1] == "{":
            stack.pop()
        elif b == "]" and stack[-1] == "[":
            stack.pop()
        elif b == ")" and stack[-1] == "(":
            stack.pop()
        # 현재 괄호와 스택의 마지막 괄호가 맞지 않으면 스택에 쌓음
        else:
            stack.append(b)
    # 스택에 괄호가 남아 있다면 모든 괄호가 닫히지 않았으므로 올바르지 않음
    if stack:
        return False
    # 스택이 비어 있다면 올바름
    else:
        return True

def solution(s):
    x = len(s)
    answer = 0
    # s를 왼쪽으로 x만큼 회전
    for _ in range(x):
        s = s[1:] + s[0]
        if correct(s):
            answer += 1
    return answer


'''
테스트 1 〉	통과 (70.73ms, 10.2MB)
테스트 2 〉	통과 (71.37ms, 10.2MB)
테스트 3 〉	통과 (91.36ms, 10.1MB)
테스트 4 〉	통과 (83.32ms, 10.1MB)
테스트 5 〉	통과 (123.06ms, 10.2MB)
테스트 6 〉	통과 (76.66ms, 10.3MB)
테스트 7 〉	통과 (74.12ms, 10.3MB)
테스트 8 〉	통과 (92.11ms, 10.2MB)
테스트 9 〉	통과 (70.71ms, 10.1MB)
테스트 10 〉	통과 (76.59ms, 10.3MB)
테스트 11 〉	통과 (79.29ms, 10.2MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
'''