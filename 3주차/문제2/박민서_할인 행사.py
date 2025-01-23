def solution(want, number, discount):
    answer = 0
    
    want_dict = {}
    
    for product in want:
        if product not in discount:
            return 0
    
    for product, num in zip(want, number):
        want_dict[product] = num
    
    for i in range(len(discount) - 9):
        check_products = discount[i:i+10]
        check_dict = {}
        
        for product in check_products:
            if product not in check_dict:
                check_dict[product] = 1
            else:
                check_dict[product] += 1
    
        answer += (want_dict == check_dict)
    
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (10.65ms, 10.6MB)
테스트 2 〉	통과 (63.59ms, 14.5MB)
테스트 3 〉	통과 (15.59ms, 11MB)
테스트 4 〉	통과 (89.79ms, 15.6MB)
테스트 5 〉	통과 (43.94ms, 12.9MB)
테스트 6 〉	통과 (6.68ms, 10.6MB)
테스트 7 〉	통과 (19.60ms, 11.5MB)
테스트 8 〉	통과 (100.86ms, 17.3MB)
테스트 9 〉	통과 (21.79ms, 11.1MB)
테스트 10 〉	통과 (53.04ms, 13.7MB)
테스트 11 〉	통과 (11.61ms, 10.4MB)
테스트 12 〉	통과 (0.00ms, 10.1MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''