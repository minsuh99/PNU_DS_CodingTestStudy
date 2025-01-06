def solution(arr1, arr2):
    answer = [[]]
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for r1 in range(0,len(arr1)):
        for c2 in range(0,len(arr2[0])):
            for r2 in range(0,len(arr2)):
                answer[r1][c2]+=arr1[r1][r2]*arr2[r2][c2]
    return answer
