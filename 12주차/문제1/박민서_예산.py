def solution(d, budget):
    answer = 0
    d = sorted(d)
    # '최대' 몇 개의 부서에게 지원이 가능한지 묻는 거니까
    # 작은 예산부터 예산을 주고 다음 부서에게 줄 남은 금액이 있으면
    # 그 다음 예산의 부서에게 부여하는게 타당함.
    
    for money in d:
        if money <= budget:
            answer += 1
            budget -= money
    
    return answer