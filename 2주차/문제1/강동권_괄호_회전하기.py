opening = {'[', '(','{'}
close = {']', ')', '}'}
matching = {')': '(', ']': '[', '}': '{'}

def valid(s):
    stack =[]
    for j in range(0,len(s)):
        next=s[j]
        if next in close:
            if not stack or stack[-1] != matching[next]:
                return False
            else:
                stack.pop()
        else:
            stack.append(next)
            
    return not stack
        
def solution(s):
    answer = 0
    for i in range(0,len(s)):
        if valid(s[i:] + s[:i]):
            answer+=1
    return answer

# 테스트 1 〉	통과 (8.07ms, 10.2MB)
# 테스트 2 〉	통과 (4.57ms, 10.1MB)
# 테스트 3 〉	통과 (4.40ms, 10.3MB)
# 테스트 4 〉	통과 (6.48ms, 10.3MB)
# 테스트 5 〉	통과 (22.62ms, 10.1MB)
# 테스트 6 〉	통과 (8.96ms, 10.4MB)
# 테스트 7 〉	통과 (13.35ms, 10.4MB)
# 테스트 8 〉	통과 (18.59ms, 10.4MB)
# 테스트 9 〉	통과 (33.83ms, 10.2MB)
# 테스트 10 〉	통과 (48.08ms, 10.1MB)
# 테스트 11 〉	통과 (73.82ms, 10.1MB)
# 테스트 12 〉	통과 (0.00ms, 10.1MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.2MB)
