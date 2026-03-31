class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = "".join([char for char in s if char.isalnum()])
        lower = new_str.lower()
        l, r = 0, len(lower)-1
        while l < r:
            if lower[l] != lower[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
    
        