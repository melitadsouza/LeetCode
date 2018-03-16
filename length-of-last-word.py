#Time Complexity: O(n), Space Complexity: O(1)


class Solution(object):
#solution 1
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])
   #solution 2     
    def lengthOfLastWord1(self, s): 
        length = 0
        for word in reversed(s):
            if word == ' ':
                if length:
                    break
            else: 
                length += 1
        return length
        
   
   
