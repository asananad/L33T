# Implement Linked List

class Node:
    def __init__(self, head):
        self.head = head
        self.next = None

first_node = Node("data1")

second_node = Node("data2")

first_node.next = second_node

print(first_node.next.head)