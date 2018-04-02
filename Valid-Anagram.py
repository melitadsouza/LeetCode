class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = s.replace(' ','').lower()
        t = t.replace(' ','').lower()
        if len(s)!=len(t):
            return False
        
        
        
        return sorted(s) == sorted(t)
        
        
        
