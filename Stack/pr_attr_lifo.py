# 괄호 유효성 문제
# 문제 단순화
# 1. 여는게 있으면 닫는게 있어야 한다 - 짝수, 짝이 맞아야함
# 2. 여는게 먼저 와야함
# 3. 괄호 종류별로 여는 괄호가 있으면 +1, 닫는 괄호가 있으면 -1
#   - 닫는 괄호가 먼저와 -1이오면 false
#   - LIFO - 마지막에 들어온 괄호를 먼저 처리하여야 한다.

s="[[{}]]()"

# stack이 비어있는지 체크
def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{":
            stack.append("{") 
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False
    return not stack

# 괄호 유효성이 stack으로 정해놓지 않고
# 왜 stack으로 구현해야 될지 생각하며 구현
# 이 문제만 보면 바로 코드가 구현될 정도로 5번 이상
# 그후 응용 확장