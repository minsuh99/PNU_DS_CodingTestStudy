def solution(cards1, cards2, goal):
    answer = "Yes"
    i1=i2=0
    for i in range(len(goal)):
        if i1<len(cards1) and goal[i]==cards1[i1]:
            i1+=1
        elif i2<len(cards2) and goal[i]==cards2[i2]:
            i2+=1
        else:
            answer="No"
            break
    return answer

# 테스트 1 〉	통과 (0.00ms, 9.96MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.00ms, 10.3MB)
# 테스트 4 〉	통과 (0.00ms, 10MB)
# 테스트 5 〉	통과 (0.00ms, 10MB)
# 테스트 6 〉	통과 (0.00ms, 10MB)
# 테스트 7 〉	통과 (0.00ms, 10MB)
# 테스트 8 〉	통과 (0.00ms, 10.1MB)
# 테스트 9 〉	통과 (0.00ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.01ms, 10.2MB)
# 테스트 13 〉	통과 (0.00ms, 10.2MB)
# 테스트 14 〉	통과 (0.01ms, 10.1MB)
# 테스트 15 〉	통과 (0.01ms, 10.1MB)
# 테스트 16 〉	통과 (0.01ms, 10MB)
# 테스트 17 〉	통과 (0.01ms, 10.2MB)
# 테스트 18 〉	통과 (0.01ms, 10.2MB)
# 테스트 19 〉	통과 (0.01ms, 10.1MB)
# 테스트 20 〉	통과 (0.01ms, 10.1MB)
# 테스트 21 〉	통과 (0.00ms, 10.1MB)
# 테스트 22 〉	통과 (0.01ms, 9.99MB)
# 테스트 23 〉	통과 (0.00ms, 10.1MB)
# 테스트 24 〉	통과 (0.00ms, 10.1MB)
# 테스트 25 〉	통과 (0.00ms, 10.1MB)
