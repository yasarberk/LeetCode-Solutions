class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for num in nums:
            if nums.index(num) != len(nums)-1:
                for i in range(nums.index(num) + 1, len(nums)):
                    if num + nums[i] == target:
                        return [nums.index(num), i]