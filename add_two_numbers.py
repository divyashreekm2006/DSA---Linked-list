"""
Problem: Add Two Numbers Represented by Linked Lists

Description: Add two non-negative numbers represented by linked lists. Each node contains one digit, with the least significant digit first.

Example::

Input:
List 1: 2 -> 4 -> 3, representing 342
List 2: 5 -> 6 -> 4, representing 465

Output: 7 -> 0 -> 8, representing 807
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def add_two_numbers(head1, head2):
    dummy = Node(0)
    current = dummy
    carry = 0

    while head1 or head2 or carry:
        x = head1.data if head1 else 0
        y = head2.data if head2 else 0

        total = x + y + carry
        carry = total // 10

        current.next = Node(total % 10)
        current = current.next

        if head1:
            head1 = head1.next

        if head2:
            head2 = head2.next

    return dummy.next


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


head1 = Node(2)
head1.next = Node(4)
head1.next.next = Node(3)

head2 = Node(5)
head2.next = Node(6)
head2.next.next = Node(4)

result = add_two_numbers(head1, head2)
print_list(result)