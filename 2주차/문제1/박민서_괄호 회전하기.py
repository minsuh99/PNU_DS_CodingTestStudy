# 연습문제 있는 코드 활용

def check_vaild_str(s: str):
    stack = [] # 문자열 담을 리스트
    mapping_table = { # 괄호 매칭할 table
                     # '(': ')'도 될 것 같으나 닫는 괄호를 이용해서 stack에 열린 괄호가 있다면
                     # 성공적으로 pop을 하는 것이니 이게 더 자연스럽다고 생각각
        ')': '(',
        '}': '{',
        ']': '[',
    }
    for char in s:
        if char not in mapping_table: # table에 없는 괄호면 stack에 push
            stack.append(char)
        elif not stack or mapping_table[char] != stack.pop(): 
            # table에 있는 괄호면 pop을 해서 매칭, 실패하면 유효하지 않은 문자열로 판단
            # **not stack**을 통해 stack이 비어있는지 아닌지를 확인 (검색해보니 많이 쓰는 방법인듯)
            return False
    return len(stack) == 0



def solution(s):
    answer = 0
    for x in range(len(s)):
        check_s = [s[(i + x) % len(s)] for i in range(len(s))] # x만큼 왼쪽으로 회전
        answer += check_vaild_str(check_s) # 결과가 유효하면 1, 아니면 0이 더해짐
    return answer

'''
테스트 1 〉	통과 (147.00ms, 10.3MB)
테스트 2 〉	통과 (142.16ms, 10.2MB)
테스트 3 〉	통과 (151.47ms, 10.3MB)
테스트 4 〉	통과 (166.61ms, 10.2MB)
테스트 5 〉	통과 (158.33ms, 10.4MB)
테스트 6 〉	통과 (149.53ms, 10.2MB)
테스트 7 〉	통과 (139.77ms, 10.2MB)
테스트 8 〉	통과 (159.59ms, 10.2MB)
테스트 9 〉	통과 (162.32ms, 10.3MB)
테스트 10 〉	통과 (171.57ms, 10.2MB)
테스트 11 〉	통과 (192.86ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.2MB)
'''