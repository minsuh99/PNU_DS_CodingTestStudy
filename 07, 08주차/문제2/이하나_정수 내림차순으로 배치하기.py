def solution(n):
    str_n = f'{n}'
    list = []
    for i in str_n:
        list.append(i)
    return int(''.join(sorted(list, reverse=True)))