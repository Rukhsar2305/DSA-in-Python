class Solution(object):
    def maxProduct(self, nums):
        
        maxProduct = nums[0]
        minProduct = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            if num < 0:
                maxProduct, minProduct = minProduct, maxProduct
            
            maxProduct = max(num, maxProduct * num)
            minProduct = min(num, minProduct * num)

            result = max(result, maxProduct)
        
        return result