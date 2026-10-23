"""
Problem: Find the Length of a Loop

Description: 
Find the number of nodes in a cycle in a linked list. Return zero if no cycle exists.

Example:
Input: 10 -> 20 -> 30 -> 40 -> 50, where node 50 points back to node 30.
Output: 3
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length_of_loop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            count = 1
            current = slow.next

            while current != slow:
                count += 1
                current = current.next

            return count

    return 0


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

# Create a loop from 50 to 30
head.next.next.next.next.next = head.next.next

print(length_of_loop(head))