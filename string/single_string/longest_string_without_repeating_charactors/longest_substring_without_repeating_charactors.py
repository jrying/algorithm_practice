# Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = ""
        longestl = 0
        current = ""
        currentl = 0
        for i in xrange(len(s)):
            if s[i] in current:
                if currentl > longestl:
                    longestl, longest = currentl, current
                j = current.index(s[i])
                currentl, current = currentl - j, current[j+1:] + s[i]
            else:
                current += s[i]
                currentl += 1
        if currentl > longestl:
            longestl, longest = currentl, current

        return longestl
