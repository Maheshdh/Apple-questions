# question link : https://leetcode.com/problems/furthest-building-you-can-reach/description/
# Time complexity : O(nlogn)
# Space complexity: O(n)
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                bricks -= diff
                heapq.heappush(heap,-diff)
                if bricks < 0:
                    if ladders > 0:
                        ladders -= 1
                        bricks += -heapq.heappop(heap)
                    else:
                        return i
        return len(heights) - 1
