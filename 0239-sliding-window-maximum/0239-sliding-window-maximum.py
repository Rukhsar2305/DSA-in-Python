class Solution(object):
    def maxSlidingWindow(self, nums, k):
        
        dq = deque()
        result = []

        for i in range(len(nums)):

            #1. Remove indices outside the window
            while dq and dq[0] <= i - k:
                dq.popleft()

            #2. Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            #3. Add current index
            dq.append(i)

            #4. Store maximum when window is complete
            if i >= k - 1:
                result.append(nums[dq[0]])
            
        return result