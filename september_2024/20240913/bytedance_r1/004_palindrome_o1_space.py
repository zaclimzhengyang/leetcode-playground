class ListNode():
    def __init__(self, next=None, val=None):
        self.next = next
        self.val = val

class Solution():
    '''
    [1,2,3,4,5,6]
    '''
    def is_palindrome(self, head: ListNode) -> bool:
        # 01 - find middle point
        fast: ListNode = head
        slow: ListNode = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 02 - reverse the second half of the linked list
        second_half: ListNode = self.reverse_linked_list(slow)
        first_half: ListNode = head

        while first_half and second_half:
            if first_half.val !=second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

    def reverse_linked_list(self, head: ListNode) -> ListNode:
        previous: ListNode = None
        while head:
            temp: ListNode = head.next
            head.next = previous
            previous = head
            head = temp
        return previous


node_5: ListNode = ListNode(next=None, val=1)
node_4: ListNode = ListNode(next=node_5, val=2)
node_3: ListNode = ListNode(next=node_4, val=3)
node_2: ListNode = ListNode(next=node_3, val=2)
node_1: ListNode = ListNode(next=node_2, val=1)

my_solution: Solution = Solution()
result: bool = my_solution.is_palindrome(node_1)
print(f'result: {result}')


node_15: ListNode = ListNode(next=None, val=10)
node_14: ListNode = ListNode(next=node_15, val=13)
node_13: ListNode = ListNode(next=node_14, val=14)
node_12: ListNode = ListNode(next=node_13, val=15)
node_11: ListNode = ListNode(next=node_12, val=16)

my_solution2: Solution = Solution()
result2: bool = my_solution2.is_palindrome(node_11)
print(f'result2: {result2}')

'''
time complexity: o(n)
space complexity: o(n)
'''