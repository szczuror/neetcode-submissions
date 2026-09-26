class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0]) # sorting by the end values

        # strictly greater to be overlapping!

        removals = 0
        prev = intervals[0]

        for start, end in intervals[1:]:
            if start >= prev[1]:
                prev = [start,end]
            else:
                # start < prevEnd
                removals += 1
                prev = [start, min(end, prev[1])]            

        return removals