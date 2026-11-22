class Solution(object):
    def checkSubarraySum(self, nums, k):
        
        remainder_map = {0: -1}
        prefix_sum = 0

        for i in range(len(nums)):

            prefix_sum += nums[i]

            if k != 0:
                remainder = prefix_sum % k
            else:
                remainder = prefix_sum

            if remainder in remainder_map:

                if i - remainder_map[remainder] >= 2:
                    return True

            else:
                remainder_map[remainder] = i
        
        return False