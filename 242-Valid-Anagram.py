class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        sCount, tCount = {}, {}

        for i in range(len(s)):
            # Get usage: If there is no s[i] in the sCount dictionary, it will return 0 automatically
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)
        return sCount == tCount
