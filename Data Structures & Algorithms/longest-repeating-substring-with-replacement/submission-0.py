class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        curr_freqs = {}
        left = 0
        max_frequency = 0

        # what we are looking for is a sequence where len-highest_frequency_letter<=k
        for right, char in enumerate(s):
            curr_freqs[char] = 1 + curr_freqs.get(char, 0)
            max_frequency = max(max_frequency, curr_freqs[char])

            while (right - left + 1) - max_frequency > k:
                curr_freqs[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        
        return res