def solution(record):
    total = []
    people = set()
    num = len(record)
    answer = []
    people_dict = {}

    for i in record:
        temp = []
        temp.append(i.split(' '))
        total += temp
    
    for i in range(num):
        people.add(total[i][1])
    
    for i in people:
        for j in total[::-1]:
            if (i == j[1]) & (j[0] != "Leave"):
                people_dict[i] = j[2]
                break
            continue
    
    print(people_dict)
    for i in range(len(total)):
        if total[i][0] == "Enter":
            word2 = "님이 들어왔습니다."
            word = people_dict[total[i][1]]

            answer.append(word+word2)
        elif total[i][0] == "Leave":
            word2 = "님이 나갔습니다."
            word = people_dict[total[i][1]]
            answer.append(word+word2)
        else:
            continue

    return answer

# 테스트 1 〉	통과 (0.02ms, 10MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.06ms, 10.1MB)
# 테스트 4 〉	통과 (0.09ms, 10.4MB)
# 테스트 5 〉	통과 (0.87ms, 10.3MB)
# 테스트 6 〉	통과 (2.10ms, 10.2MB)
# 테스트 7 〉	통과 (0.78ms, 10.2MB)
# 테스트 8 〉	통과 (2.09ms, 10.4MB)
# 테스트 9 〉	통과 (24.99ms, 10.3MB)
# 테스트 10 〉	통과 (2.25ms, 10.5MB)
# 테스트 11 〉	통과 (6.18ms, 10.3MB)
# 테스트 12 〉	통과 (6.49ms, 10.2MB)
# 테스트 13 〉	통과 (1.97ms, 10.3MB)
# 테스트 14 〉	통과 (23.66ms, 10.3MB)
# 테스트 15 〉	통과 (0.03ms, 10.1MB)
# 테스트 16 〉	통과 (0.03ms, 10.1MB)
# 테스트 17 〉	통과 (0.10ms, 10.2MB)
# 테스트 18 〉	통과 (0.09ms, 10MB)
# 테스트 19 〉	통과 (1.39ms, 10.3MB)
# 테스트 20 〉	통과 (1.13ms, 10.3MB)
# 테스트 21 〉	통과 (0.97ms, 10.4MB)
# 테스트 22 〉	통과 (1.55ms, 10.2MB)
# 테스트 23 〉	통과 (1.12ms, 10.6MB)
# 테스트 24 〉	통과 (1.45ms, 10.6MB)
# 테스트 25 〉	실패 (시간 초과)
# 테스트 26 〉	실패 (시간 초과)
# 테스트 27 〉	실패 (시간 초과)
# 테스트 28 〉	실패 (시간 초과)
# 테스트 29 〉	실패 (시간 초과)
# 테스트 30 〉	실패 (시간 초과)
# 테스트 31 〉	실패 (시간 초과)
# 테스트 32 〉	실패 (시간 초과)