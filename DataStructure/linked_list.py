# 리스트의 노드 부분
class ListNode :
    def __init__(self, data, next=None) :
        self.data = data
        self.next = next

def printNodes(node:ListNode) :
    crnt_node = node
    while crnt_node is not None :
        print(crnt_node.data, end=' ')
        crnt_node = crnt_node.next

# 연결 리스트
class LinkedList :
    def __init__(self) :
        self.head = None
        
    # O(1)
    def addAtHead(self, data) :
        node = ListNode(data)
        node.next = self.head
        self.head = node

    # O(N)
    # but when the list
    def addBack(self, data) :
        node = ListNode(data)
        crnt_node = self.head
        while crnt_node.next :
            crnt_node = crnt_node.next
        crnt_node.next = node

    # O(N)
    def findNode(self, data) :
        crnt_node = self.head
        while crnt_node is not None :
            if crnt_node.data == data :
                return crnt_node
            crnt_node = crnt_node.next
        raise RuntimeError('Node not found')

    # O(1)
    def addAfter(self, node, data) :
        new_node = ListNode(data)
        new_node.next = node.next
        node.next = new_node

    # O(1)
    def deleteAfter(self, prev_node) :
        if prev_node.next is not None :
            prev_node.next = prev_node.next.next

# main
if __name__ == "__main__" :
    pass