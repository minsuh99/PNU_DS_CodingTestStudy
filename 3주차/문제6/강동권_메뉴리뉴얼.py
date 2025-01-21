from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for num in course:
        menu = Counter()  
        
        for customer in orders:
            # Sort the customer 
            customer = ''.join(sorted(customer)) # nees string to be used as key
            
            # Generate all combinations of length 'num' from the sorted customer order
            for combo in combinations(customer, num):
                menu[''.join(combo)] += 1 # counter creates the key if non-existent  
        # Find the highest count for combinations with at least 2 occurrences
        max_count = max(menu.values(), default=0)
      
        if max_count>=2:# count>=2 needed because there could be none
            for combo, count in menu.items():
                if count == max_count:
                    answer.append(combo)
    
    return sorted(answer)


# 테스트 1 〉	통과 (0.12ms, 10.1MB)
# 테스트 2 〉	통과 (0.11ms, 9.95MB)
# 테스트 3 〉	통과 (0.16ms, 10.1MB)
# 테스트 4 〉	통과 (0.17ms, 10.1MB)
# 테스트 5 〉	통과 (0.14ms, 10.2MB)
# 테스트 6 〉	통과 (0.24ms, 9.96MB)
# 테스트 7 〉	통과 (0.47ms, 10.2MB)
# 테스트 8 〉	통과 (3.55ms, 10.1MB)
# 테스트 9 〉	통과 (1.33ms, 10.1MB)
# 테스트 10 〉	통과 (2.07ms, 10.2MB)
# 테스트 11 〉	통과 (1.06ms, 10.1MB)
# 테스트 12 〉	통과 (2.23ms, 10.2MB)
# 테스트 13 〉	통과 (2.88ms, 10.3MB)
# 테스트 14 〉	통과 (1.25ms, 10.3MB)
# 테스트 15 〉	통과 (2.43ms, 10.2MB)
# 테스트 16 〉	통과 (0.46ms, 10.2MB)
# 테스트 17 〉	통과 (0.46ms, 10MB)
# 테스트 18 〉	통과 (0.13ms, 10.1MB)
# 테스트 19 〉	통과 (0.04ms, 10.1MB)
# 테스트 20 〉	통과 (0.32ms, 10.2MB)
