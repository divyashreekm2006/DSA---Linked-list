"""
Problem: Reverse a Linked List in Groups of K

Description: Reverse the nodes of a linked list in groups of k. In this version, leave the final group unchanged if it contains fewer than k nodes.

Example:
Input: 10 -> 20 -> 30 -> 40 -> 50 -> 60, k = 2
Output: 20 -> 10 -> 40 -> 30 -> 60 -> 50
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_in_groups(head, k):
    if k <= 1 or head is None:
        return head

    current = head
    count = 0

    while current and count < k:
        current = current.next
        count += 1

    if count < k:
        return head

    previous = None
    current = head
    count = 0

    while current and count < k:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
        count += 1

    head.next = reverse_in_groups(current, k)

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
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)

head = reverse_in_groups(head, 2)
print_list(head)