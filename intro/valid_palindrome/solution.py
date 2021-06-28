class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def is_char_valid(self, char):
        return char.isdigit() or char.isalpha()

    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.is_char_valid(s[left]):
                left += 1
            while left < right and not self.is_char_valid(s[right]):
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True