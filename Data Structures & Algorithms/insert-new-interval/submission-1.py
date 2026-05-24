class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        i = 0
        new_intervals = []
        # while 
        # o--o
        #      x--x
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            new_intervals.append(intervals[i])
            i += 1

        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        new_intervals.append(newInterval)

        while i < len(intervals):
            new_intervals.append(intervals[i])
            i += 1

        return new_intervals