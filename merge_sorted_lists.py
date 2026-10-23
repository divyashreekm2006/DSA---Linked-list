"""
Problem: Merge Two Sorted Linked Lists

Description : Merge two linked lists sorted in ascending order into a single sorted linked list.

Example

Input:
List 1: 10 -> 30 -> 50
List 2: 20 -> 40 -> 60
Output: 10 -> 20 -> 30 -> 40 -> 50 -> 60
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_sorted_lists(head1, head2):
    dummy = Node(0)
    current = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next

        current = current.next

    current.next = head1 if head1 else head2

    return dummy.next


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


head1 = Node(10)
head1.next = Node(30)
head1.next.next = Node(50)

head2 = Node(20)
head2.next = Node(40)
head2.next.next = Node(60)

head = merge_sorted_lists(head1, head2)
print_list(head)