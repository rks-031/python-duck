class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_str = ""
        for i in range(len(s)):
            if s[i].isalnum():
                lower_str += s[i]
        
        lower_str = lower_str.lower()
        s = 0
        e = len(lower_str) - 1

        while(s<e):
            if lower_str[s] != lower_str[e]:
                return False
            s+=1
            e-=1
        
        return True