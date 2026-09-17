class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        
        n1 = len(s1)
        n2 = len(s2)
        pattern_freqs = {}
        current_freqs = {}

        for char in s1:
            pattern_freqs[char] = pattern_freqs.get(char, 0) + 1

        for i in range(n1):
            current_freqs[s2[i]] = current_freqs.get(s2[i], 0) + 1 # preprocessing


        if pattern_freqs == current_freqs:
                return True

        for r in range(n1, n2):
            current_freqs[s2[r]] = current_freqs.get(s2[r], 0) + 1
            left_char = s2[r-n1]
            current_freqs[left_char] -= 1
            if current_freqs[left_char] == 0:
                del current_freqs[left_char]

            if pattern_freqs == current_freqs:
                return True

        return False

        