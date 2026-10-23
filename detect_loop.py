"""
Problem: Detect a Loop in a Linked List

Description: Determine whether a linked list contains a cycle using Floyd's slow and fast pointer algorithm.

Example:
Input: 10 -> 20 -> 30 -> 40, where node 40 points back to node 20.
Output: True
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def detect_loop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

# Create a loop: 40 points to 20
head.next.next.next.next = head.next

print(detect_loop(head))