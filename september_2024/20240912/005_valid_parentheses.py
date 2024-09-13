from typing import Dict, List


class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open: Dict[str,str] = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        open_stack: List[str] = []
        for curr in s:
            if curr not in close_to_open:
                open_stack.append(curr)
            else:
                if len(open_stack) > 0 and open_stack[-1] == close_to_open[curr]:
                    open_stack.pop()
                else:
                    return False
        return len(open_stack) == 0

my_solution = Solution()
print(my_solution.isValid("()[]{}"))
print(my_solution.isValid("()[[]{}"))