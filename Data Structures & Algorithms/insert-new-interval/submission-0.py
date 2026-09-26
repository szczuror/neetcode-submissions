class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find two intervals to fit newInterval between in 
        startIdx = endIdx = -1
        newStart, newEnd = newInterval[0], newInterval[1]
        first, second = newStart, newEnd

        for idx, interval in enumerate(intervals):
            currStart = interval[0]
            currEnd = interval[1]
            # situations to consider:
            # currentInterval starts fits between one interval, then we need to find another interval when the
            # end matches
            
            if currStart <= newEnd and currEnd >= newStart:
                if startIdx == -1:
                    startIdx = idx
                endIdx = idx
                first = min(first, currStart)
                second = max(second, currEnd)

        # now we have both end idx and start idx, between those we need to merge intervals
        # it would probably be better to merge them on the fly
        res = []
        # 4 cases in total: no intersectiong, intersection only on the left, only on the right and both
        if startIdx == -1:
            # no intersection found at all
            inserted = False
            for interval in intervals:
                if not inserted and interval[0] > newEnd:
                    res.append([newStart, newEnd])
                    inserted = True
                res.append(interval)
            if not inserted: # last elem
                res.append([newStart, newEnd])
        else:
            # we have start so we must to have the end as well -- the end may be the same idx as the start tho
            for idx, interval in enumerate(intervals):
                if idx < startIdx:
                    res.append(interval)
                elif idx == startIdx:
                    res.append([first, second])
                if idx > endIdx:
                    res.append(interval)
        return res
