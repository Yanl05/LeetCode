# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)
        res = []
        for i in range(len(intervals)):
            if res == []:
                res.append(intervals[i])
            else:
                size = len(res)
                if res[size-1].start <= intervals[i].start <= res[size-1].end:
                    res[size-1].end = max(res[size-1].end, intervals[i].end)
                else:
                    res.append(intervals[i])
        return res

intervals = []
for item in ([[1,2],[3,5],[6,7],[8,10],[12,16]]):
    tmp = Interval(item[0], item[1])
    intervals.append(tmp)
newInterval = Interval(4, 8)
# print(intervals[0].start)
print(Solution().insert(intervals, newInterval))
