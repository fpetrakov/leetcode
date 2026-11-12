class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda interval: interval.start)

        for index, curr in enumerate(intervals):
            if index == 0:
                continue

            prev_end = intervals[index - 1].end

            if prev_end > curr.start:
                return False

        return True
