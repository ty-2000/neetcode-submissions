class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort intervals in ascending order by the start time
        # Iterate from the beginning
        # If the iterating interval is overlapping with the previous interval -> merge the two
        #  set the end to the larger endtime between the current one and the previous one

        if len(intervals) == 0: return []

        intervals.sort()
        new_intervals = [intervals[0]]

        i = 1
        while i < len(intervals):
            if intervals[i][0] <= new_intervals[-1][1]: # Overlapping
                new_intervals[-1][1] = max(intervals[i][1], new_intervals[-1][1])
            else: # Not overlapping
                new_intervals.append(intervals[i])
            i += 1
        
        return new_intervals