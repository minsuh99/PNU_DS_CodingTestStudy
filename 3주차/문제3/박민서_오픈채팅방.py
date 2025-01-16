def solution(record):
    answer = []
    new_records = []
    
    name_list = {}
    
    for rec in record:
        new_records.append(rec.split())
        if rec.split()[0] == "Leave":
            act, uid = map(str, rec.split())
        else:
            act, uid, nickname = map(str, rec.split())
            name_list[uid] = nickname # 들여쓰기 안해서 처음에 틀렸음
        
    
    for rec in new_records:
        uid = rec[1]
        if rec[0] == "Leave":
            message = f'{name_list[uid]}님이 나갔습니다.'
        elif rec[0] == 'Enter':
            message = f'{name_list[uid]}님이 들어왔습니다.'
        elif rec[0] == 'Change':
            continue
        answer.append(message)
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.07ms, 10.2MB)
테스트 4 〉	통과 (0.07ms, 10.3MB)
테스트 5 〉	통과 (1.55ms, 10.4MB)
테스트 6 〉	통과 (1.53ms, 10.3MB)
테스트 7 〉	통과 (1.89ms, 10.5MB)
테스트 8 〉	통과 (1.68ms, 10.4MB)ㅉㅉ
테스트 9 〉	통과 (1.69ms, 10.5MB)
테스트 10 〉	통과 (1.66ms, 10.5MB)
테스트 11 〉	통과 (0.86ms, 10.3MB)
테스트 12 〉	통과 (1.04ms, 10.4MB)
테스트 13 〉	통과 (1.77ms, 10.4MB)
테스트 14 〉	통과 (1.65ms, 10.5MB)
테스트 15 〉	통과 (0.02ms, 10.2MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
테스트 17 〉	통과 (0.23ms, 10.2MB)
테스트 18 〉	통과 (0.24ms, 10.2MB)
테스트 19 〉	통과 (2.95ms, 10.3MB)
테스트 20 〉	통과 (2.43ms, 10.4MB)
테스트 21 〉	통과 (1.59ms, 10.5MB)
테스트 22 〉	통과 (1.58ms, 10.4MB)
테스트 23 〉	통과 (1.55ms, 10.6MB)
테스트 24 〉	통과 (1.59ms, 10.5MB)
테스트 25 〉	통과 (218.39ms, 60.6MB)
테스트 26 〉	통과 (243.14ms, 65.9MB)
테스트 27 〉	통과 (234.37ms, 70.5MB)
테스트 28 〉	통과 (242.18ms, 73MB)
테스트 29 〉	통과 (242.33ms, 72.8MB)
테스트 30 〉	통과 (228.42ms, 65.1MB)
테스트 31 〉	통과 (200.36ms, 68.5MB)
테스트 32 〉	통과 (172.21ms, 58.4MB)
채점 결과
정확성: 100.0
합계: 100.0 / 100.0
'''