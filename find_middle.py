"""
Problem: Find the Middle of a Linked List

Description: Find the middle node of a linked list using slow and fast pointers. For an even-length list, return the second middle node.

Example
Input: 10 -> 20 -> 30 -> 40 -> 50
Output: 30
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data if slow else None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print(find_middle(head))