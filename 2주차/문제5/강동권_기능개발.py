import math

def solution(progresses, speeds):
    answer = []
    release_date = [0]*100
    for i,p in enumerate(progresses):
        progresses[i]=math.ceil((100-p)/speeds[i])-1
    max=0
    for p in progresses:
        if p<=max:
            answer[-1]+=1
        else:
            answer.append(1)
            max=p
    return answer

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.04ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.1MB)
# 테스트 4 〉	통과 (0.02ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.4MB)
# 테스트 7 〉	통과 (0.03ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.03ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
