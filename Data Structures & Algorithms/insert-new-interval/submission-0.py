class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        intervals.append(newInterval) # is this in place or not?
        intervals.sort(key=lambda i: i[0])
        output.append(intervals[0])

        for start, end in intervals[1:]:
            lastEndTime = output[-1][1]

            if (start <= lastEndTime):
                output[-1][1] = max(end, lastEndTime)
            else:
                output.append([start, end])
            
        return output
        