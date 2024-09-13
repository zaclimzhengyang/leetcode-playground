class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted: str = sorted(s)
        t_sorted: str = sorted(t)
        return s_sorted == t_sorted


my_solution = Solution()
print(my_solution.isAnagram("anagram", "nagarak"))
print(my_solution.isAnagram("treat", "reatt"))