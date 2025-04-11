class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        l, r = 1, x

        while l <= r:
            mid = (l + r) // 2
            print("mid:", mid)
            mid_squared = mid * mid
            print("midSquared:", mid_squared)

            if mid_squared == x:
                return mid

            elif mid_squared < x:
                l = mid + 1
            
            else:
                r = mid - 1
            
        return r



        