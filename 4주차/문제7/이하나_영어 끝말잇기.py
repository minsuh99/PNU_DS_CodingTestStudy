def solution(n, words):
    answer1 = []
    answer2 = []
    answer = []
    num1 = 100
    num2 = 100
    count = len(words)
    
    for i in range(count-1):
        if words[i][-1] != words[i+1][0]:
            num1 = i
            if ((i+2) % n) == 0:
                answer1.append(n)
            else:
                answer1.append((i+2) % n)
            if ((i+2) % n) == 0:
                answer1.append((i+2) // n)
            else:
                answer1.append(((i+2) // n)+1)
            break
    
    if (count == len(set(words))) and answer1 == []:
        answer = [0, 0]
    
    if answer != [0, 0]:
        temp = []
        for i in range(count):
            if words[i] in temp:
                num2 = i
                if ((i+1) % n) == 0:
                    answer2.append(n)
                else:
                    answer2.append((i+1) % n)
                if ((i+1) % n) == 0:
                    answer2.append((i+1) // n)
                else:
                    answer2.append(((i+1) // n)+1)
                break
            else:
                temp.append(words[i])
    
    if answer != [0, 0]:
        if (num1+1) <= num2: # 이부분도 +1 필요했음
            answer = answer1
        else:
            answer = answer2
    
    return answer

# 75% 성공 >> 이유: () 괄호 연산자 없어서 연산자 우선순위 문제
# 90% 성공 >> 이유: 끝말잇기에서 여러 요소 중 먼저 일어나는 게 다를 수 있음
# 처음엔 그냥 하나만 걸려라 해서 순서 상관없이 진행함


# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (0.04ms, 10.2MB)
# 테스트 5 〉	통과 (0.07ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.2MB)
# 테스트 7 〉	통과 (0.04ms, 10.2MB)
# 테스트 8 〉	통과 (0.04ms, 10.2MB)
# 테스트 9 〉	통과 (0.06ms, 10.2MB)
# 테스트 10 〉	통과 (0.09ms, 10.3MB)
# 테스트 11 〉	통과 (0.11ms, 10.3MB)
# 테스트 12 〉	통과 (0.03ms, 10.2MB)
# 테스트 13 〉	통과 (0.04ms, 10.3MB)
# 테스트 14 〉	통과 (0.02ms, 10.2MB)
# 테스트 15 〉	통과 (0.01ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.3MB)
# 테스트 17 〉	통과 (0.01ms, 10.4MB)
# 테스트 18 〉	통과 (0.02ms, 10.4MB)
# 테스트 19 〉	통과 (0.01ms, 10.2MB)
# 테스트 20 〉	통과 (0.10ms, 10.4MB)