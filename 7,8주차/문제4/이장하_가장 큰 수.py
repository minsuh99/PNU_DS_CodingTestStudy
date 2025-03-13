def solution(numbers):
    # 퀵 정렬 구현
    def Sort(x):
        if len(x) <= 1:
            return x
        
        pivot = x[len(x)//2]
        left, right, equal = [], [], []
        for a in x:
            if a + pivot < pivot + a:
                right.append(a)
            elif a + pivot > pivot + a:
                left.append(a)
            else:
                equal.append(a)
        return Sort(left) + equal + Sort(right)
    
    numbers = list(map(str, numbers))
    return str(int("".join(Sort(numbers))))

'''
정확성  테스트
테스트 1 〉    통과 (1088.14ms, 19.5MB)
테스트 2 〉    통과 (424.93ms, 15.3MB)
테스트 3 〉    통과 (1795.82ms, 22.2MB)
테스트 4 〉    통과 (13.86ms, 10.5MB)
테스트 5 〉    통과 (1001.75ms, 19MB)
테스트 6 〉    통과 (761.73ms, 17.7MB)
테스트 7 〉    통과 (0.06ms, 10.3MB)
테스트 8 〉    통과 (0.04ms, 10.5MB)
테스트 9 〉    통과 (0.06ms, 10.5MB)
테스트 10 〉    통과 (0.06ms, 10.3MB)
테스트 11 〉    통과 (0.06ms, 10.3MB)
테스트 12 〉    통과 (0.03ms, 10.4MB)
테스트 13 〉    통과 (0.02ms, 10.5MB)
테스트 14 〉    통과 (0.04ms, 10.5MB)
테스트 15 〉    통과 (0.04ms, 10.3MB)
'''
