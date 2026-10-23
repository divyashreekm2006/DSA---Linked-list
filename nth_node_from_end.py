"""
problem: Find the Nth Node from the End

Description: Given a linked list and an integer n, find the nth node from the end. The last node is position 1.

Example
Input: 10 -> 20 -> 30 -> 40 -> 50, n = 2
Output: 40
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def nth_node_from_end(head, n):
    if n <= 0:
        return None

    first = head
    second = head

    for _ in range(n):
        if first is None:
            return None
        first = first.next

    while first:
        first = first.next
        second = second.next

    return second.data if second else None


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print(nth_node_from_end(head, 2))