#Time Complexity: O(n), Space Complexity: O(1)
class Solution(object):
    def countSegments(self, s):
        return len(s.strip().split())
