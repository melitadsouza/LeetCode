class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        opening_brackets = set('{[(')
        matches = set([('(',')'),('{','}'),('[',']')])
        if len(s)%2 != 0:
            return False
        
        if s[0] not in opening_brackets:
            return False
        
        if not s:
            return True

        stack = []
        for parenthesis in s:
            if parenthesis in opening_brackets:
                stack.append(parenthesis)
            else:
                if len(stack) == 0:
                    return False
                last_open = stack.pop()
                if (last_open,parenthesis) not in matches:
                    return False
        return len(stack) == 0
