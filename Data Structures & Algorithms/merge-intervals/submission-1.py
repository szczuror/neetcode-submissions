class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # sorting based on starts O(nlogn)

        # merge existing intervals:p
        res = []

        current = intervals[0]

        for intervalStart, intervalEnd in intervals[1:]:
            if intervalStart <= current[1]:
                current[1] = max(current[1], intervalEnd)
                continue
            res.append(current)
            current = [intervalStart, intervalEnd]
        res.append(current)

        return res