"""
Problem: Remove Duplicates from a Sorted Linked List

Description: Remove duplicate values from a sorted linked list so that each value appears only once.

Example:

Input: 10 -> 10 -> 20 -> 30 -> 30 -> 40
Output: 10 -> 20 -> 30 -> 40
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates_sorted(head):
    current = head

    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


head = Node(10)
head.next = Node(10)
head.next.next = Node(20)
head.next.next.next = Node(30)
head.next.next.next.next = Node(30)
head.next.next.next.next.next = Node(40)

head = remove_duplicates_sorted(head)
print_list(head)