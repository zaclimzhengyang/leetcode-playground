class ListNode():
    def __init__(self, next=None, val=None):
        self.next = next
        self.val = val

class Solution():
    def reverse_linked_list(self, head: ListNode) -> ListNode:
        previous: ListNode = None
        while head:
            temp: ListNode = head.next
            head.next = previous
            previous = head
            head = temp
        return previous

    def print(self, head: ListNode) -> list[int]:
        result: list[int] = []
        while head:
            result.append(head.val)
            head = head.next
        print(f'linked_list: {result}')

node_15: ListNode = ListNode(next=None, val=16)
node_14: ListNode = ListNode(next=node_15, val=15)
node_13: ListNode = ListNode(next=node_14, val=14)
node_12: ListNode = ListNode(next=node_13, val=13)
node_11: ListNode = ListNode(next=node_12, val=12)

my_solution: Solution = Solution()
my_solution.print(node_11)

reversed_linked_list: ListNode = my_solution.reverse_linked_list(node_11)
my_solution.print(reversed_linked_list)