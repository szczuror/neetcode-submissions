class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        vals = self.store[key]

        left, right = 0, len(vals) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2

            ts = vals[mid][0]

            if ts <= timestamp:
                res = vals[mid][1]
                left = mid + 1
            else:
                right = mid -1
        return res