class Solution:
    def mergeOverlap(self, intervals):
        intervals.sort()
        ans=[]
        current=intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=current[1]:
                current[1]=max(current[1],intervals[i][1])
            else:
                ans.append(current)
                current = intervals[i]
        ans.append(current)
        return ans