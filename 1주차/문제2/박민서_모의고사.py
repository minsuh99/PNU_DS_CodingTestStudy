def solution(answers):
    answer = []
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    ans1 = [1, 2, 3, 4, 5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == ans1[i%len(ans1)]:
            cnt1 += 1
        if answers[i] == ans2[i%len(ans2)]:
            cnt2 += 1
        if answers[i] == ans3[i%len(ans3)]:
            cnt3 += 1
    
    max_cnt = max(max(cnt1, cnt2), cnt3)
    if cnt1 == max_cnt:
        answer.append(1)
    if cnt2 == max_cnt:
        answer.append(2)
    if cnt3 == max_cnt:
        answer.append(3)
    
    return answer

# 메모리: 10.4 MB, 시간: 3.43 ms
# 시간복잡도: O(n)?
# 코드 단순화 시킬 필요는 있을 것 같다.
