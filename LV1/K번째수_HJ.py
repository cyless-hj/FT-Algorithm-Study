def solution(array, commands):
    answer = []
    for com in commands:
        a = sorted(array[com[0] - 1: com[1]])
        answer.append(a[com[2] - 1])
    return answer