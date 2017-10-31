# Definition for singly-linked list
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

def detect_cycle(head):
    """

    :param head: <Node> Head of the linked list
    :return: <bool> True if it contains a cycle, False if it doesn't
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False

        slow = slow.next
        fast = fast.next.next

    return True
