class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = "".join(c.lower() for c in s if c.isalnum())
        # cleaned text. Now to check if it is a palindrome.
        n = len(alphanumeric)

        left = 0
        right = n - 1
        while(left < right):
            if (alphanumeric[left] != alphanumeric[right]):
                return False
            left += 1
            right -= 1

        return True