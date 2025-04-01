from collections import defaultdict

def solution(record):
    answer = []
    nick_table = defaultdict(str)

    # 방에 입장하거나 닉을 변경하는 경우 닉네임 테이블에 저장
    for r in record:
        if r[0] != "L":
            act, uid, nick = r.split()
            nick_table[uid] = nick

    # 방에 입장하거나 나가는경우 닉네임 테이블에 저장된 최종 닉네임을 출력
    for r in record:
        if r[0] == "E":
            answer.append(nick_table[r.split()[1]] + "님이 들어왔습니다.")
        elif r[0] == "L":
            answer.append(nick_table[r.split()[1]] + "님이 나갔습니다.")

    return answer


'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.1MB)
테스트 5 〉	통과 (1.02ms, 10.1MB)
테스트 6 〉	통과 (0.55ms, 10.3MB)
테스트 7 〉	통과 (0.44ms, 10.3MB)
테스트 8 〉	통과 (0.59ms, 10.4MB)
테스트 9 〉	통과 (0.68ms, 10.3MB)
테스트 10 〉	통과 (0.55ms, 10.4MB)
테스트 11 〉	통과 (0.58ms, 10.3MB)
테스트 12 〉	통과 (0.40ms, 10.1MB)
테스트 13 〉	통과 (0.55ms, 10.4MB)
테스트 14 〉	통과 (0.68ms, 10.2MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.06ms, 10.2MB)
테스트 18 〉	통과 (0.05ms, 10MB)
테스트 19 〉	통과 (0.79ms, 10.2MB)
테스트 20 〉	통과 (0.91ms, 10.2MB)
테스트 21 〉	통과 (0.67ms, 10.3MB)
테스트 22 〉	통과 (0.83ms, 10.2MB)
테스트 23 〉	통과 (0.58ms, 10.5MB)
테스트 24 〉	통과 (0.62ms, 10.2MB)
테스트 25 〉	통과 (68.78ms, 38.7MB)
테스트 26 〉	통과 (79.28ms, 39.4MB)
테스트 27 〉	통과 (93.64ms, 41.3MB)
테스트 28 〉	통과 (92.67ms, 42.4MB)
테스트 29 〉	통과 (86.87ms, 42.4MB)
테스트 30 〉	통과 (75.64ms, 36.4MB)
테스트 31 〉	통과 (125.72ms, 41MB)
테스트 32 〉	통과 (56.40ms, 38.2MB)
'''