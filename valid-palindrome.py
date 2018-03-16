#Time Complexity: O(n), Space Complexity: O(1)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
       """

        s = s.lower()
        start = 0
        end = len(s) - 1
        while start <= end:
            
            if s[start]==s[end]:
                start += 1
                end -= 1
                continue
                
            if s[start].isalnum() and s[end].isalnum() and s[start] != s[end]:
                return False
            elif s[start].isalnum():
                end -= 1
            else:
                start += 1
        return True
                
