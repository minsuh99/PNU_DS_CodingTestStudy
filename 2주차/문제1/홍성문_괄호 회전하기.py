# 초기 코드 if is_correct(s) 함수를 못짜겠음..이건 포기..

def is_correct(s):
    string = []
    for s in string:

    return 

def solution(s):
    answer = 0

    for i in range(len(s)):
        s = s[i:]+s[:i]
        if is_correct(s) :
            answer +=1
    
    return answer


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
print(solution("}}}"))

# (), [], {} 다 올바른 괄호
# 안에 들어가면 다 올바른 괄호
# 두개 연속해도 올바른 괄호
