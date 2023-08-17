class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        temp = ""

        for i in s:
            if(i.isalnum()):
                temp += i.lower()
        
        return temp == temp[::-1]
