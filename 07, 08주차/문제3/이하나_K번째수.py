def solution(array, commands):
    temp = []
    answer = []
    for i in commands:
        temp = sorted(array[i[0]-1:i[1]])
        print(temp)
        answer.append(temp[i[2]-1])            
    return answer
