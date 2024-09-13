class ListNode():
    def __init__(self, next=None, val=None):
        self.next = next
        self.val = val

class Solution():
    def is_palindrome(self, head: ListNode) -> bool:
        value_list: list[int] = []
        while head:
            curr: int = head.val
            value_list.append(curr)
            head = head.next

        value_list_len: int = len(value_list)
        for i in range(value_list_len // 2):
            if value_list[i] != value_list[value_list_len - i - 1]:
                return False

        return True


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