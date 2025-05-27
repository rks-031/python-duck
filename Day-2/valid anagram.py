# Approach 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        t1 = {}

        for i in range(len(s)):
            s1[s[i]] = s1.get(s[i], 0) + 1
        
        for i in range(len(t)):
            t1[t[i]] = t1.get(t[i], 0) + 1

        for k,v in t1.items():
            if k not in s1 or v!=s1[k]:
                return False

        return len(t) == len(s)

# Approach 2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = ''.join(sorted(s))
        t1 = ''.join(sorted(t))

        if s1!=t1:
            return False

        return True 