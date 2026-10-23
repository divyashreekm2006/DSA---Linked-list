"""
Problem: Find the Intersection Point of Two Linked Lists

Description: Find the first node shared by two linked lists. Intersection means the same node in memory, not just equal values.

Example::

List 1: 10 -> 20 -> 30 -> 40
List 2: 15 -> 25 -> 30 -> 40

Assume both lists share the actual nodes containing 30 and 40.
Output: 30
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_intersection(head1, head2):
    p1 = head1
    p2 = head2

    while p1 != p2:
        p1 = p1.next if p1 else head2
        p2 = p2.next if p2 else head1

    return p1.data if p1 else None


# Shared nodes
shared1 = Node(30)
shared2 = Node(40)
shared1.next = shared2

# First list
head1 = Node(10)
head1.next = Node(20)
head1.next.next = shared1

# Second list
head2 = Node(15)
head2.next = Node(25)
head2.next.next = shared1

print(find_intersection(head1, head2))