class Solution:
    def isPalindrome(self, s: str) -> bool:
        revString = ""
        for i in s:
            if i.isalnum():
                revString += i.lower()
        return revString == revString[::-1]