"""
Problem: Check Whether a Linked List Is a Palindrome

Description: Determine whether the linked list reads the same forward and backward.

Example:

Input: 10 -> 20 -> 30 -> 20 -> 10
Output: True
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def is_palindrome(head):
    values = []
    current = head

    while current:
        values.append(current.data)
        current = current.next

    return values == values[::-1]


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(20)
head.next.next.next.next = Node(10)

print(is_palindrome(head))