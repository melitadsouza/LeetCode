#Time Complexity: O(logx), Space Complexity: O(1)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
       
        if (x==0 or x == 1):
            return x
        if x < 4:
            return 1
        start = 0
        end = x
        for i in range(0,1000):

            mid = (start + end)//2
            if (mid * mid == x):
                return mid
            if (mid * mid < x):
                start = mid

            else: 
                end = mid
        return mid
        
