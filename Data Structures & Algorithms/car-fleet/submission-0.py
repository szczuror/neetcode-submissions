class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars_n = len(position) # same as len of speed
        # positions are unique

        # cars behind affect the cars in the front -- sort them by position descending ig
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for pos,spd in cars:
            time = (target - pos) / spd # arrival at, we add to the stack only distinct times of arrival.

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)