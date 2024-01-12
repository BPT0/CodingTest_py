# tuple 및 stack 활용
# 특정조건이 되면 데이터를 pop 하는 형식
# stack[-1] 은 top의 데이터를 가리킴
# prev_day, _ 튜플에 stack의 pop 한 값을 저장

def dailyTemperatures(temp):
    answer = [0] * len(temp)
    stack = []
    for day, temp in enumerate(temp):
        while stack and stack[-1][1] < temp:
            prev_day, _ = stack.pop() # _는 temp를 의미하나요?
            answer[prev_day] = day - prev_day # 이부분 이해가 되지 않아 설명이 막힘 다시 수강하기
        stack.append((day, temp)) 
    return answer

dailyTemperatures([73,74,75,71,69,72,76,73])