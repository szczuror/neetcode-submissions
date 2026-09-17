class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns, nt = len(s), len(t)

        if nt > ns or nt == 0:
            return ""
        
        l, r = 0, nt

        # variable size sliding window?
        shortest = float('inf')
        result = [-1, -1]
        source_map = {}
        for char in t:
            source_map[char] = source_map.get(char, 0) + 1
        
        curr_map = {}
        
        l = 0
        have, need = 0, len(source_map)
        for r in range(ns):
            curr = s[r]
            curr_map[curr] = 1 + curr_map.get(curr, 0)

            if curr in source_map and source_map[curr] == curr_map[curr]:
                have += 1
            
            while have == need: # trying to shorten the window
                if (r - l + 1) < shortest:
                    shortest = r - l + 1
                    result = [l, r]

                curr_map[s[l]] -= 1
                if s[l] in source_map and curr_map[s[l]] < source_map[s[l]]:
                    have -= 1
                l += 1

        left, right = result
        if shortest != float('inf'):
            return s[left : right + 1]
        return ""