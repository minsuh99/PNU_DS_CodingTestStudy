def solution(N, stages):
    stuck=[0]*N
    completed=[0]*N
    answer = []
    
    for stage in stages:
        for i in range(0,stage-1):
            completed[i]+=1
        if stage-1 !=N:
            stuck[stage-1]+=1
    
    errorRates=[0]*N
    
    for i in range(0,N):
        if completed[0]+stuck[0]:
            errorRates[i]=stuck[i]/(completed[i]+stuck[i])
        else:
            errorRates[i]=0
    answer=sorted(range(len(errorRates)), key=lambda i: (-errorRates[i], i))
    for i in range(0,len(answer)):
        answer[i]+=1
        
    return answer
