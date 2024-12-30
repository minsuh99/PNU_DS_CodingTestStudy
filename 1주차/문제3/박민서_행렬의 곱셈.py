def solution(arr1, arr2):
    final_row = len(arr1)
    final_col = len(arr2[0])
    
    # answer = [[0] * final_col] * final_row
    # 이렇게 하면 독립적인 수정이 불가능
    
    answer = [[0 for _ in range(final_col)] for _ in range(final_row)]

    for row in range(final_row):
        for col in range(final_col):
            mat_sum = sum(arr1[row][k] * arr2[k][col] for k in range(len(arr2)))
            answer[row][col] = mat_sum
    return answer

# 메모리: 10.9 MB, 시간: 79.22 ms
# 시간 복잡도: O(n^3) 예상
# 5행 때문에 푸는데 오래 걸림
