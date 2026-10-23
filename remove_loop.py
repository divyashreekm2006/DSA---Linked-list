"""
Problem: Remove a Loop from a Linked List

Description: Detect and remove a cycle without deleting any nodes.

Example:
Input: 10 -> 20 -> 30 -> 40 -> 50, where node 50 points back to node 30.
Output: 10 -> 20 -> 30 -> 40 -> 50 -> None
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_loop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return head

    slow = head

    if slow == fast:
        while fast.next != slow:
            fast = fast.next
    else:
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

    fast.next = None
    return head


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

head.next.next.next.next.next = head.next.next

remove_loop(head)
print_list(head)