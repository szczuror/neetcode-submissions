class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        window = set()

        for idx, char in enumerate(s):
            while char in window:
                window.remove(s[left])
                left += 1
            window.add(char)
            result = max(result, idx - left + 1)

        return result