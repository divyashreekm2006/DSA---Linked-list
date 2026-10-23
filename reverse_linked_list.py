"""
Problem: Reverse a Linked List

Description: Reverse the links between nodes so that the last node becomes the first node.

Example
Input: 10 -> 20 -> 30 -> 40
Output: 40 -> 30 -> 20 -> 10
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

head = reverse_linked_list(head)
print_list(head)