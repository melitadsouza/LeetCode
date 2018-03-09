class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
         # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b:
            carry = a & b
            a = (a ^ b)&mask
            b = (carry << 1)&mask 
            
        return a if a <= MAX else ~(a ^ mask)
