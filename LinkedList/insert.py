class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node= Node(value)
        if self.head is None:
            self.head = new_node
    def insert(self, idx, value):
        if(idx == 0):
            current = self.head
        else:
            current = self.head
            # current가 idx번 이전 노드를 가리키게 head에서 idx 번 이동
            for i in range(idx-1):
                current = current.next
        # 삽입할 노드의 다음 노드를 임시로 저장
        front_node = current.next
        # 노드 생성
        insert_node = Node(value)
        # 다음 노드에 노드 삽입
        current.next = insert_node
        # 삽입한 노드의 next에 이후에 front_node 저장 
        insert_node.next = front_node
    def remove_at(self, idx):
        current = self.head
        # current를 idx 까지 노드 이동
        while(current.value == idx):
            current = current.next
        # 삽입할 노드의 다음 노드를 임시로 저장
        front_node = current.next
    
class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next
        
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.insert(idx=2, value=9)
ll.remove_at(idx=3)