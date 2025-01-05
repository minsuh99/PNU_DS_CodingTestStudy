def solution(answers):
    answer = []
    scores = []
    score = 0
    k=1
    for i in range(0,len(answers)):
        if answers[i] == k :
            score += 1
        k +=1
        if k == 6 :
            k == 1
    scores.append(score)
    score = 0
    k=1
    for i in range(0,len(answers)):
        if i%2==0:
            if answers[i] == 2 :
                score += 1
        else:
            if answers[i] == k :
                score += 1
            k +=1
            if k == 6 :
                k == 1
            elif k == 2 :
                k+=1
    scores.append(score)
    score = 0
    k=[3,1,2,4,5]
    for i in range(0,len(answers)):
        temp=i%10
        if answers[i] == k[i//2] :
                score += 1
    scores.append(score)
    highest_score=max(scores)
    for i in range(0,3):
        if scores[i]==highest_score:
            answer.append(i+1)
    return answer
