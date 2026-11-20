class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        output = []

        # sort results by start time
        intervals.sort(key=lambda i: i[0]) 
        output.append(intervals[0]) # append first input for later edge case

        # loop through all but first element
        for start,end in intervals[1:]:
            lastEndTime = output[-1][1]

            if start <= lastEndTime:
                output[-1][1] = max(end, lastEndTime)
            else:
                output.append([start, end])
        return output
 
        