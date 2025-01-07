def solution(progresses, speeds):
    answer = []
    stack = [] # 작업 일수 담을 stack
    work_days = [0 for _ in range(len(progresses))] # 배포하는데 걸린 일수를 기록할 리스트
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            work_days[i] = (100 - progresses[i]) // speeds[i] # 100%로 딱 떨어지면 몫만
        else:
            work_days[i] = (100 - progresses[i]) // speeds[i] + 1 # 아니면 하루 더 걸려야 작업 완료 (math.celi 쓰면 될 거 같은데 안 됨)
    
    for day in work_days:
        if not stack or max(stack) >= day: # stack[-1] >= day로 했다가 오답 / 배포하려는 기능보다 작은 값들이 들어가기 때문에 마지막 값만 비교하는게 아닌, 가장 큰 값(작업이 가장 오래 걸렸던 일수)을 비교하는게 맞음
            stack.append(day)
        else:
            answer.append(len(stack))
            stack.clear()
            stack.append(day)
    answer.append(len(stack))
    return answer


# 분명 큐 문제인데 성질 이용 안하고 품
# collections.deque를 사용하고 싶었지만 넘어감

'''
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.18ms, 10.1MB)
테스트 3 〉	통과 (0.05ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.3MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.04ms, 10.1MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.1MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
'''