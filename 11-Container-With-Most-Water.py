class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        maxField = 0

        l, r = 0, len(height)-1

        while l < r:

            amount = min(height[l], height[r]) * (r-l)
            maxField = max(maxField, amount)

            if (height[l] > height[r]):
                r -= 1
            elif (height[l] < height[r]):
                l += 1
            else:
                l += 1
        
        return maxField
