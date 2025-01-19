from collections import Counter

def solution(want, number, discount):
    answer = 0
    sl = {key: value for key, value in zip(want, number)}

    for i in range(0,len(discount)-9):
        discount_count = Counter(discount[i:i+10])
        valid=1
        for key, value in sl.items():  
            if discount_count[key] < value:  
                valid = 0
                break
        if valid:
            answer += 1
        
    return answer
