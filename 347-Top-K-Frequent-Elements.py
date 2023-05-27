class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dic = {}

        for num in nums:
            dic[num] = 1 + dic.get(num, 0) 

        dic = sorted(dic.items(), key=lambda x:x[1])

        arr = []
        
        for i in range(-1, -1-k, -1):
            arr.append(dic[i][0])   
        
        return arr