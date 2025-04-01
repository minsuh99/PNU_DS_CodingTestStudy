def solution(prices):
    l = len(prices)
    answer = [0]*l
    stack = []

    # 인덱스와 함께 반복
    for i, price in enumerate(prices):
        # 스택에 값이 있고, 현재 가격이 스택의 마지막 가격보다 떨어진 경우
        while stack and price < stack[-1][1]:
            # 마지막 가격을 스택에서 빼고
            last, _ = stack.pop()
            # 해당 가격의 초를 현재 초에서 뺀 차이만큼 기록
            answer[last] = i - last
        # 스택에 현재 초와 가격을 쌓음
        stack.append((i, price))

    # 끝까지 가격이 떨어지지 않은 기록이 stack에 남아 있으므로 전체 시간에서 뺀만큼 기록
    for i, price in stack:
        answer[i] = l - i -1

    return answer


'''
정확성 테스트
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.1MB)
테스트 3 〉	통과 (0.25ms, 10.4MB)
테스트 4 〉	통과 (0.47ms, 10.3MB)
테스트 5 〉	통과 (0.31ms, 10.2MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.17ms, 10.4MB)
테스트 8 〉	통과 (0.21ms, 10.4MB)
테스트 9 〉	통과 (0.02ms, 10.2MB)
테스트 10 〉	통과 (0.30ms, 10.2MB)

효율성 테스트
테스트 1 〉	통과 (24.67ms, 18.8MB)
테스트 2 〉	통과 (18.46ms, 17.6MB)
테스트 3 〉	통과 (27.48ms, 19.3MB)
테스트 4 〉	통과 (20.55ms, 18.2MB)
테스트 5 〉	통과 (14.75ms, 16.9MB)
'''