def solution(answers):
    answer = []
    scores = [0,0,0]
    k1=1
    k2=1
    k=[3,1,2,4,5]
    for i in range(0,len(answers)):
        if answers[i] == k1 :
            scores[0] += 1
        k1 +=1
        if k1 == 6 :
            k1 == 1
        if i%2==0:
            if answers[i] == 2 :
                scores[1] += 1
        else:
            if answers[i] == k2 :
                scores[1] += 1
            k2 +=1
            if k2 == 6 :
                k2 == 1
            elif k2 == 2 :
                k2+=1
        temp=i%10
        if answers[i] == k[i//2] :
                scores[2] += 1
    highest_score=max(scores)
    
    for i in range(0,3):
        if scores[i]==highest_score:
            answer.append(i+1)
            
    return answer
