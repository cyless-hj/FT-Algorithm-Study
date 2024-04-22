def solution(participant, completion):
    dic = {}
    for part in participant: # dic에 참가자 이름 별 수 형태로 넣어준다.
        dic[part] = dic.get(part, 0) + 1
        
    for comp in completion: # dic value에서 완주자 1명씩 빼준다.
        dic[comp] = dic.get(comp) - 1
    
    answer = [k for k, v in dic.items() if v > 0][0] # 완주하지 못한 1명 추출
    return answer