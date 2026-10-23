"""
Problem: Search in Linked List

Description:
Given a linked list and a target value, check whether the target exists in the list.

Example:
Input: 10 -> 20 -> 30 -> 40, Target = 30
Output: True
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def search_linked_list(head, target):
    current = head

    while current:
        if current.data == target:
            return True
        current = current.next

    return False


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print(search_linked_list(head, 30))