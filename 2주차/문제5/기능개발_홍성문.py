def solution(progresses, speeds):
    workday = []
    answer = []

    for i in range(len(progresses)):
        remain = 100 - progresses[i] #걸리는 작업 일수 계산
        day = remain // speeds[i]

        if remain % speeds[i] !=0: #나머지있으면 +1
            day +=1
        workday.append(day)

    count = 0

    for j in workday:
        if j <= workday[0]:
            count +=1
        else:
            answer.append(count)
            count =1 # 초과하면 무조건 1개로 새로 시작
            workday[0] = j #배포기준일 새로 지정

    answer.append(count)


    return answer



print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.04ms, 10.1MB)
# 테스트 3 〉	통과 (0.04ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.1MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.01ms, 10.2MB)
# 테스트 7 〉	통과 (0.03ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.02ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)