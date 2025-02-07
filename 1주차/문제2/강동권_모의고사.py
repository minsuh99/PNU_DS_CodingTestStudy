def solution(answers):
    answer = []
    scores = [0,0,0]
    k1=[1,2,3,4,5]
    k2=1
    k3=[3,1,2,4,5]
    for i in range(0,len(answers)):
        curAnswer=answers[i]
        if curAnswer == k1[i%5] :
            scores[0] += 1
        if i%2==0:
            if curAnswer == 2 :
                scores[1] += 1
        else:
            if curAnswer == k2 :
                scores[1] += 1
            k2 +=1
            if k2 == 6 :
                k2 = 1
            elif k2 == 2 :
                k2+=1
        temp=i%10
        if curAnswer == k3[(i//2)%5] :
                scores[2] += 1
    
    highest_score=max(scores)
    
    for i in range(0,3):
        if scores[i]==highest_score:
            answer.append(i+1)

# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.01ms, 10.3MB)
# 테스트 4 〉	통과 (0.01ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.4MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (1.54ms, 10.2MB)
# 테스트 8 〉	통과 (0.51ms, 10.1MB)
# 테스트 9 〉	통과 (2.66ms, 10.4MB)
# 테스트 10 〉	통과 (1.24ms, 10.2MB)
# 테스트 11 〉	통과 (3.03ms, 10.2MB)
# 테스트 12 〉	통과 (2.69ms, 10.2MB)
# 테스트 13 〉	통과 (0.18ms, 10.2MB)
# 테스트 14 〉	통과 (2.82ms, 10.3MB)
