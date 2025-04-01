def solution(s):
    total = []
    for i in s:
        if i == "{":
            temp = []
            a = ""
        elif i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
            a = a + i
        elif i == ",":
            if len(a) != 0:
                temp.append(int(a))
            a = ""
        elif i == "}":
            if len(a) != 0:
                temp.append(int(a))
                a = ""
            if len(temp) != 0:
                total.append(temp)
    
    total.sort(key=len)
    
    answer = []
    for i in total:
        for j in i:
            if j not in answer:
                answer.append(j)
                
    return answer


# 테스트 1 〉	통과 (0.03ms, 9.42MB)
# 테스트 2 〉	통과 (0.03ms, 9.48MB)
# 테스트 3 〉	통과 (0.03ms, 9.29MB)
# 테스트 4 〉	통과 (0.12ms, 9.46MB)
# 테스트 5 〉	통과 (0.72ms, 9.52MB)
# 테스트 6 〉	통과 (2.21ms, 9.39MB)
# 테스트 7 〉	통과 (45.52ms, 9.96MB)
# 테스트 8 〉	통과 (168.71ms, 11.5MB)
# 테스트 9 〉	통과 (96.23ms, 10.7MB)
# 테스트 10 〉	통과 (205.28ms, 11.7MB)
# 테스트 11 〉	통과 (442.55ms, 12.6MB)
# 테스트 12 〉	통과 (514.09ms, 14.9MB)
# 테스트 13 〉	통과 (489.89ms, 14.8MB)
# 테스트 14 〉	통과 (509.08ms, 14.9MB)
# 테스트 15 〉	통과 (0.03ms, 9.44MB)