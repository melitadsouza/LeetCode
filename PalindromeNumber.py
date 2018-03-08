class Solution:
    def isPalindrome(self, x): 
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        num = x
        result = 0
        while x:
            result = result*10 + x%10
            x = x//10
        return True if result == num else False
        
