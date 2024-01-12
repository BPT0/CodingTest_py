# 괄호 유효성 문제
s="[[{}]]()"

def chk_bracket(s):
    stack = []
    for p in s:
        if(p == '['):
            stack.pop(']')
        elif(p == '{'):
            stack.pop('}')
        elif(p == '('):
            stack.pop(')')
        elif not stack or stack.pop != p:
            return False
    return not stack

"""
    1.주어진 매개변수 주의하지 않음
        반복문을 돌면서 순회하는 것 놓침
    2. stack에는 s가 여는 괄호가 올때 
        닫는 괄호를 추가
    3. 반복문을 돌면서 stack에 아무 값도 없거나 
        닫는 괄호가올때
        다음에 오는 문자열과 일치하지 않으면
        false 반환
    4. 반복문을 다 돌고 stack에 남은 값 
        없으면 반환
    
    문제 플때 유의하기 
    손으로 문제의 상황을 구체적으로 생각하고
    문제를 최대화, 최소화 해서 생각해보기 
    파라미터의 형식을 유의하자
    내가 리턴해서 분류할 값에 유의하자
"""