def solution(record):
    users = {}
    log=[]
    answer = []
    for s in record:
        parts = s.split()
        action = parts[0]
        uid = parts[1]
        
        if action in ("Enter", "Change"):
            nickname = parts[2]
            users[uid] = nickname  
            
        if action != "Change":
            log.append((action, uid))
            
    for l in log:
        action=l[0]
        uid=l[1]
        nickname=users[uid]
        if action == "Enter":
            answer.append(f"{nickname}님이 들어왔습니다.")
        else :
            answer.append(f"{nickname}님이 나갔습니다.")
    
    return answer


# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 9.96MB)
# 테스트 4 〉	통과 (0.06ms, 10.1MB)
# 테스트 5 〉	통과 (0.67ms, 10.4MB)
# 테스트 6 〉	통과 (0.74ms, 10.2MB)
# 테스트 7 〉	통과 (0.57ms, 10.2MB)
# 테스트 8 〉	통과 (0.82ms, 10.5MB)
# 테스트 9 〉	통과 (0.78ms, 10.5MB)
# 테스트 10 〉	통과 (0.73ms, 10.2MB)
# 테스트 11 〉	통과 (0.37ms, 10.5MB)
# 테스트 12 〉	통과 (0.39ms, 10.1MB)
# 테스트 13 〉	통과 (0.68ms, 10.3MB)
# 테스트 14 〉	통과 (0.81ms, 10.5MB)
# 테스트 15 〉	통과 (0.01ms, 10MB)
# 테스트 16 〉	통과 (0.01ms, 10.1MB)
# 테스트 17 〉	통과 (0.08ms, 10.2MB)
# 테스트 18 〉	통과 (0.11ms, 10.1MB)
# 테스트 19 〉	통과 (0.84ms, 10.3MB)
# 테스트 20 〉	통과 (0.55ms, 10.3MB)
# 테스트 21 〉	통과 (0.54ms, 10.3MB)
# 테스트 22 〉	통과 (0.58ms, 10.3MB)
# 테스트 23 〉	통과 (0.73ms, 10.4MB)
# 테스트 24 〉	통과 (0.90ms, 10.5MB)
# 테스트 25 〉	통과 (83.68ms, 49.7MB)
# 테스트 26 〉	통과 (100.42ms, 57.4MB)
# 테스트 27 〉	통과 (117.39ms, 60.2MB)
# 테스트 28 〉	통과 (117.90ms, 61.6MB)
# 테스트 29 〉	통과 (106.60ms, 61.4MB)
# 테스트 30 〉	통과 (73.55ms, 43.4MB)
# 테스트 31 〉	통과 (80.23ms, 51.3MB)
# 테스트 32 〉	통과 (74.86ms, 46.2MB)
