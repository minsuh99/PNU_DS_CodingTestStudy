from itertools import combinations

def solution(orders, course):
    answer = []
    
    order_dict = {}
    
    for order in orders:
        temp = [s for s in order]
        for k in course:
            if len(temp) < k:
                continue
            else:
                for comb in list(combinations(temp, k)):
                    food = " ".join(comb).split()
                    food = "".join(sorted(comb))
                    if food in order_dict:
                        order_dict[food] += 1
                    else:
                        order_dict[food] = 1
                        
    print(order_dict)
    for k in course:
        try:
            most_order = max([value for key, value in order_dict.items() if (len(key) == k) and (value > 1)])
        except:
            continue
        best_food = [key for key, value in order_dict.items() if (len(key) == k) and (value == most_order)]
        print(most_order)
        answer.extend(best_food)
        answer.sort()
            
    return answer

# 효율성 테스트 있으면 무조건 0점


'''
정확성  테스트
테스트 1 〉	통과 (0.17ms, 10MB)
테스트 2 〉	통과 (0.10ms, 10.2MB)
테스트 3 〉	통과 (0.17ms, 10.2MB)
테스트 4 〉	통과 (0.19ms, 10.2MB)
테스트 5 〉	통과 (0.19ms, 10.2MB)
테스트 6 〉	통과 (0.48ms, 10.2MB)
테스트 7 〉	통과 (0.52ms, 10.1MB)
테스트 8 〉	통과 (4.91ms, 10.3MB)
테스트 9 〉	통과 (3.64ms, 10.4MB)
테스트 10 〉	통과 (4.54ms, 10.6MB)
테스트 11 〉	통과 (2.40ms, 10.6MB)
테스트 12 〉	통과 (3.17ms, 10.4MB)
테스트 13 〉	통과 (5.09ms, 10.6MB)
테스트 14 〉	통과 (5.48ms, 10.6MB)
테스트 15 〉	통과 (6.43ms, 10.3MB)
테스트 16 〉	통과 (1.66ms, 10.2MB)
테스트 17 〉	통과 (0.55ms, 10.4MB)
테스트 18 〉	통과 (0.21ms, 10.4MB)
테스트 19 〉	통과 (0.05ms, 10.4MB)
테스트 20 〉	통과 (0.68ms, 10.3MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''