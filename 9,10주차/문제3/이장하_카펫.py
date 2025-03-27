def solution(brown, yellow):
    # xy = yellow, x >= y --> yellow >= y^2
    for y in range(1, int(yellow ** 0.5) + 1):
        # 길이는 정수
        if yellow % y == 0:
            x = yellow // y
            # 갈색은 노란색 가로 세로 합의 두배에 모서리 4를 더한 값
            if 2 * (x + y) == brown - 4:
                return [x + 2, y + 2]
    return


'''
정확성  테스트
테스트 1 〉    통과 (0.01ms, 9.32MB)
테스트 2 〉    통과 (0.02ms, 9.3MB)
테스트 3 〉    통과 (0.12ms, 9.2MB)
테스트 4 〉    통과 (0.02ms, 9.26MB)
테스트 5 〉    통과 (0.02ms, 9.32MB)
테스트 6 〉    통과 (0.04ms, 9.3MB)
테스트 7 〉    통과 (0.08ms, 9.3MB)
테스트 8 〉    통과 (0.10ms, 9.18MB)
테스트 9 〉    통과 (0.20ms, 9.23MB)
테스트 10 〉    통과 (0.15ms, 9.18MB)
테스트 11 〉    통과 (0.01ms, 9.19MB)
테스트 12 〉    통과 (0.01ms, 9.27MB)
테스트 13 〉    통과 (0.02ms, 9.24MB)
'''
