def solution(enroll, referral, seller, amount):
    answer = []
    
    answer_dict = {} # 정답을 담을 dict
    tree_dict = {} # 등록인과 추천인을 담을 dict
    
    for enr in enroll:
        answer_dict[enr] = 0
        
        # 이 과정을 안 하려면 defaultdict를 쓰는게 좋았을듯
        
    for enr, ref in zip(enroll, referral):
        if ref != "-":
            tree_dict[enr] = ref
    # 추천인 저장 {등록 : 추천}
    
    for sell, m in zip(seller, amount):
        cur = sell
        profit = m * 100
        # 재귀적인 반복이 필요 -> while문 적용해본것
        # 수익에서 10%만 떼간 만큼을 최종적으로 더하면 됨
        """ # 처음 코드 (생각나는대로 하다보니 복잡해지고 연산이 많아짐)
        while True:
            if cur not in tree_dict:
                if int(profit * 0.1) == 0:
                    answer_dict[cur] += profit
                else:
                    answer_dict[cur] += (profit - int(profit * 0.1))
                break
            else:
                if int(profit * 0.1) == 0:
                    answer_dict[cur] += profit
                else:
                    answer_dict[cur] += (profit - int(profit * 0.1))
                cur = tree_dict[cur]
                profit = int(profit * 0.1)
        """
        
        while cur != "-" and profit > 0:
            answer_dict[cur] += (profit - (profit // 10))
            cur = tree_dict.get(cur, "-") # 수정, 
            # tree_dict에서 cur라는 key (등록인)를 입력했을때, value (추천인)이 나오는,, 아니면 "-"(center)
            profit //= 10
                
    answer = list(answer_dict.values())
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.1MB)
테스트 2 〉	통과 (0.15ms, 10.2MB)
테스트 3 〉	통과 (0.07ms, 10.1MB)
테스트 4 〉	통과 (0.13ms, 10.2MB)
테스트 5 〉	통과 (0.92ms, 10.2MB)
테스트 6 〉	통과 (2.21ms, 12.6MB)
테스트 7 〉	통과 (2.29ms, 12.5MB)
테스트 8 〉	통과 (5.63ms, 12.4MB)
테스트 9 〉	통과 (28.13ms, 13.3MB)
테스트 10 〉	통과 (171.39ms, 21.1MB)
테스트 11 〉	통과 (148.02ms, 20.5MB)
테스트 12 〉	통과 (139.57ms, 20.5MB)
테스트 13 〉	통과 (160.12ms, 20.5MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''