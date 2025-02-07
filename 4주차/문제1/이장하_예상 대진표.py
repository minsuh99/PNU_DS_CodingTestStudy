def solution(n,a,b):
    for i in range(1, n//2 + 1):
        # 해당 라운드에서 몇번째 게임을 하는지 계산
        a = (a+1)//2
        b = (b+1)//2
        
        # 같은 게임을 하는경우 서로가 맞붙음
        if a == b:
            return i

    return


'''
정확성  테스트
테스트 1 〉    통과 (0.00ms, 9.95MB)
테스트 2 〉    통과 (0.00ms, 10.1MB)
테스트 3 〉    통과 (0.00ms, 10.2MB)
테스트 4 〉    통과 (0.00ms, 10.4MB)
테스트 5 〉    통과 (0.00ms, 10.2MB)
테스트 6 〉    통과 (0.00ms, 10.2MB)
테스트 7 〉    통과 (0.00ms, 10MB)
테스트 8 〉    통과 (0.00ms, 10.1MB)
테스트 9 〉    통과 (0.00ms, 10.3MB)
테스트 10 〉    통과 (0.00ms, 10.1MB)
테스트 11 〉    통과 (0.00ms, 10.2MB)
테스트 12 〉    통과 (0.01ms, 10.3MB)
테스트 13 〉    통과 (0.00ms, 10MB)
테스트 14 〉    통과 (0.00ms, 10.1MB)
테스트 15 〉    통과 (0.00ms, 10.2MB)
테스트 16 〉    통과 (0.00ms, 10.1MB)
테스트 17 〉    통과 (0.00ms, 10.2MB)
테스트 18 〉    통과 (0.00ms, 10.2MB)
테스트 19 〉    통과 (0.00ms, 9.96MB)
테스트 20 〉    통과 (0.00ms, 9.96MB)
테스트 21 〉    통과 (0.00ms, 9.95MB)
테스트 22 〉    통과 (0.00ms, 9.91MB)
테스트 23 〉    통과 (0.01ms, 10.1MB)
테스트 24 〉    통과 (0.00ms, 10.3MB)
테스트 25 〉    통과 (0.00ms, 10.2MB)
테스트 26 〉    통과 (0.00ms, 10.1MB)
테스트 27 〉    통과 (0.01ms, 10.2MB)
테스트 28 〉    통과 (0.01ms, 10.2MB)
테스트 29 〉    통과 (0.01ms, 10.2MB)
테스트 30 〉    통과 (0.01ms, 10.1MB)
테스트 31 〉    통과 (0.01ms, 10.1MB)
테스트 32 〉    통과 (0.00ms, 10.3MB)
테스트 33 〉    통과 (0.01ms, 10.2MB)
테스트 34 〉    통과 (0.01ms, 10.2MB)
'''

