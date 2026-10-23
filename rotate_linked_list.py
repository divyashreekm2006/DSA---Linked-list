"""
Problem : Rotate a linked list

Description: Rotate a linked list to the right by K positions

Example: 
Input: 10 -> 20 -> 30 -> 40 -> 50,k =2
output : 40 -> 50-> ->10 ->20 ->30
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def rotate_linked_list(head, k):
    if head is None or head.next is None or k == 0:
        return head

    length = 1
    tail = head

    while tail.next:
        tail = tail.next
        length += 1

    k = k % length

    if k == 0:
        return head

    tail.next = head

    steps_to_new_tail = length - k
    new_tail = head

    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head


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

head = rotate_linked_list(head, 2)
print_list(head)
    