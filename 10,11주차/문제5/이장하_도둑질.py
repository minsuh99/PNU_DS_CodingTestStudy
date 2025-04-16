def solution(money):
    # 첫번째 집을 터는 경우
    money1 = [0] + money[:-1]
    # 안터는 경우
    money2 = [0] + money[1:]
    for i in range(3, len(money)):
        # 직전 집은 못털고 2,3번째 이전 집중 비싼 곳을 털기
        money1[i] += max(money1[i-2], money1[i-3])
        money2[i] += max(money2[i-2], money2[i-3])
    # 마지막집과 마지막 직전집을 턴 경우중 최댓값
    answer = max(money1[-1], money1[-2], money2[-1], money2[-2])
    return answer


'''
정확성  테스트
테스트 1 〉    통과 (0.21ms, 9.08MB)
테스트 2 〉    통과 (0.58ms, 9.33MB)
테스트 3 〉    통과 (0.31ms, 9.15MB)
테스트 4 〉    통과 (0.03ms, 9.24MB)
테스트 5 〉    통과 (0.16ms, 9.08MB)
테스트 6 〉    통과 (0.36ms, 9.17MB)
테스트 7 〉    통과 (0.45ms, 9.13MB)
테스트 8 〉    통과 (0.17ms, 9.14MB)
테스트 9 〉    통과 (0.85ms, 9.16MB)
테스트 10 〉    통과 (0.12ms, 9.07MB)
효율성  테스트
테스트 1 〉    통과 (563.76ms, 115MB)
테스트 2 〉    통과 (523.54ms, 108MB)
테스트 3 〉    통과 (516.49ms, 113MB)
테스트 4 〉    통과 (518.10ms, 114MB)
테스트 5 〉    통과 (491.55ms, 95.5MB)
테스트 6 〉    통과 (497.29ms, 109MB)
테스트 7 〉    통과 (289.13ms, 67.7MB)
테스트 8 〉    통과 (300.74ms, 69.3MB)
테스트 9 〉    통과 (352.54ms, 80MB)
테스트 10 〉    통과 (504.06ms, 110MB)
'''
