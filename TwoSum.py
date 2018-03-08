class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums)<2:
            return
    
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:   
                
                
                return [seen[target - num], i]
            seen[num] = i
                       
