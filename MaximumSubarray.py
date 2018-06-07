class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        
       
        Sum = 0
        result = nums[0]
        
        if nums == []:
            return 0
        if max(nums) < 0:
            return max(nums)
        for i in range(len(nums)):
            
            
            Sum = Sum + nums[i]

            if Sum < 0:
                
                Sum = 0
                i = i + 1
            result =  max(result,Sum)
            
            
        return result
        
