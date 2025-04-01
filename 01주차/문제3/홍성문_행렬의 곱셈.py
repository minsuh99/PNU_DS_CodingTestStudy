def solution(arr1, arr2):
    answer = []


    for _ in range(len(arr1)):  # arr1의 행 개수만큼 반복
        row = [0] * len(arr2[0])  # arr2의 열 개수만큼 0으로 채운 리스트 생성
        answer.append(row)  # 생성한 행(row)을 answer에 추가
# 초기 행렬 만들어되는지 몰라서 GPT한테 물어봄..
        
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k] * arr2[k][j]
                
    return answer

#메모리: MB, 시간:  ms