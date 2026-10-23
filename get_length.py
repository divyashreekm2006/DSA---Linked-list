"""
Problem: Length of Linked List

Description: Given the head of a linked list, find the total number of nodes.

Example
Input: 10 -> 20 -> 30 -> 40
Output: 4
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def get_length(head):
    count = 0
    current = head

    while current:
        count += 1
        current = current.next

    return count


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print(get_length(head))