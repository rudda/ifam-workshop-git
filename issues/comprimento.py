class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        string = s.strip()
        string_with_no_blanks = string.split(" ")
        last_word = string_with_no_blanks[-1]
        len_last_word = len(last_word)

        return len_last_word