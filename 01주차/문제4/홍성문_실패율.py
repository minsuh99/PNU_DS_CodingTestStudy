def solution(N, stages):
    answer=[] 
    whole_ppl = len(stages)
    
    for i in range(1,N+1):
        not_clear = stages.count(i)
        
        if whole_ppl != 0:
            fail = not_clear / whole_ppl
        else:
            fail = 0
            
        answer.append((i,fail))
        whole_ppl -= not_clear

    # 실패율 기준 내림차순 정렬 (같은 경우 스테이지 번호 오름차순)
    answer = sorted(answer, key=lambda x: (-x[1], x[0]))
    # 스테이지 번호만 추출
    # return [i for i, _ in answer]
    return answer


#내림차순 정렬부분 몰라서 gpt한테 물어봄..
#메모리: MB, 시간:  ms
