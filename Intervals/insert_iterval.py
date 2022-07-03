
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        response = []
        # start value of the newInterval given
        start = newInterval[0]
        # end value of the newInterval given
        end = newInterval[1]

        for i in range(len(intervals)):
        # if the end is less than the intervals[i] start value
            if end < intervals[i][0]:
        # add the newInterval to the response array + all subarrays start from i element up to the end
                response.append(newInterval)
                return response + intervals[i:]
        # if the start is grater than the intervals[i]end value
        # just add the intervals[i] subarray
            elif start > intervals[i][1]:
                response.append(intervals[i])
        # otherwise assignt the minimum value from start and intervals[i]start and the maximum value end and intervals[i]end
        # to the newInterval here we are merging the overlap values
            else:
                newInterval = [min(start, intervals[i][0]),max(end, intervals[i][1])]
        # add newInterval to the response array                
            response.append(newInterval)
            return response
