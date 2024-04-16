from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people)) # 오름차순 정렬
    
    while people:
        if len(people) == 1: # 1명인 경우 answer +1 하고 끝
            answer += 1
            break
        
        if people[0] + people[-1] <= limit: # 가장 가벼운 사람 + 가장 무거운 사람 <= limit
            people.pop() # 가장 무거운 사람 제거
            people.popleft() # 가장 가벼운 사람 제거
        else: # limit 보다 무거우면
            people.pop() # 가장 무거운 사람 1명만 제거
        answer += 1

    return answer