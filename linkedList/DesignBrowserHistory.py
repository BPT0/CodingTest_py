# step수 만큼 코드 실행에 100(N) 이기에 시간 복잡도를 고려하지 않아도 됨
# vist, back, foward 는 최대 5000번의 호출이 있을 수 있음 
# -> 알고리즘에 영향 있을수 있음
# visit 메소드 기능을 구현하기 위해 Linked List 중간에 추가삽입 용이

# Worst Case
#   - visit(100)
#   - back(100) or forward(100), 약4900번

class ListNode:
    def __init__(self, value = 0, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    def __init__(self, homepage):
        # *연속할당: 가장 우측의 값을 좌측의 변수에 동시에 할당
        self.head = self.current = ListNode(value= homepage)
        
    def visit(self, url):
        self.current.next = ListNode(value=url, prev=self.current)
        self.current = self.current.next
        return None
    
    def back(self, steps):
        while(steps>0 and self.current.prev !=None):
            self.current = self.current.prev
            steps -= 1
        return self.current.value
    
    def forward(self, steps):
        while(steps>0 and self.current.next !=None):
            self.current = self.current.next
            steps -= 1
        return self.current.value
