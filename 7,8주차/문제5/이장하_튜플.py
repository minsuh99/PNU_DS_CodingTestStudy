def solution(s):
    answer = []
    tuples = sorted(list(s[2:-2].split("},{")), key = len)
    for idx, tup in enumerate(tuples):
        tup = list(tup.split(","))
        i = 0
        while i <= idx:
            if int(tup[i]) not in answer:
                answer.append(int(tup[i]))
            i += 1
                
    return answer

'''
정확성  테스트
테스트 1 〉    통과 (0.03ms, 10.3MB)
테스트 2 〉    통과 (0.03ms, 10.3MB)
테스트 3 〉    통과 (0.03ms, 10.3MB)
테스트 4 〉    통과 (0.07ms, 10.3MB)
테스트 5 〉    통과 (0.31ms, 10.2MB)
테스트 6 〉    통과 (0.80ms, 10.3MB)
테스트 7 〉    통과 (30.39ms, 10.3MB)
테스트 8 〉    통과 (134.47ms, 11MB)
테스트 9 〉    통과 (72.20ms, 10.5MB)
테스트 10 〉    통과 (205.01ms, 10.8MB)
테스트 11 〉    통과 (207.23ms, 11.2MB)
테스트 12 〉    통과 (362.51ms, 12MB)
테스트 13 〉    통과 (301.67ms, 12MB)
테스트 14 〉    통과 (387.41ms, 12MB)
테스트 15 〉    통과 (0.02ms, 10.2MB)
'''
